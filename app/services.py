from sqlalchemy.orm import Session
from . import models
from .utils import get_current_cycle_number, cache_current_question, get_cached_current_question
from datetime import datetime, timedelta
from pytz import timezone

async def get_current_question_for_region(db: Session, region: models.Region):
    # Try to get the question from cache
    question_id = await get_cached_current_question(region.id)
    if question_id:
        question = db.query(models.Question).filter(models.Question.id == int(question_id)).first()
        return question

    # If not cached, calculate the current question
    cycle_number = get_current_cycle_number(db, region)
    if cycle_number is None:
        return None

    questions = db.query(models.Question).join(
        models.question_region_association
    ).filter(
        models.question_region_association.c.region_id == region.id
    ).order_by(
        models.Question.position_in_cycle
    ).all()

    question_count = len(questions)
    if question_count == 0:
        return None

    question_index = cycle_number % question_count
    question = questions[question_index]

    # Cache the question for the remaining duration of the cycle
    config = region.cycle_config
    now = datetime.now(timezone('UTC'))
    time_until_next_cycle = ((config.start_time + timedelta(days=(cycle_number + 1) * config.duration)) - now).total_seconds()
    await cache_current_question(region.id, question, int(time_until_next_cycle))

    return question
