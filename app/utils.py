from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from . import models
from pytz import timezone
import redis.asyncio as redis
from . import models
from .database import settings



redis_client = redis.Redis.from_url(settings.REDIS_URL, encoding="utf-8", decode_responses=True)

async def cache_current_question(region_id: int, question: models.Question, ttl: int):
    cache_key = f"current_question_region_{region_id}"
    await redis_client.set(cache_key, question.id, ex=ttl)

async def get_cached_current_question(region_id: int):
    cache_key = f"current_question_region_{region_id}"
    question_id = await redis_client.get(cache_key)
    return question_id

    now = datetime.now(timezone('UTC'))
    time_elapsed = now - config.start_time
    cycle_number = time_elapsed.days // config.duration
    return cycle_number
