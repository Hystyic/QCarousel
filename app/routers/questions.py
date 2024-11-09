from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas, services, dependencies, auth

router = APIRouter()

@router.get("/question/", response_model=schemas.Question)
async def get_current_question(current_user: models.User = Depends(auth.get_current_user), db: Session = Depends(dependencies.get_db)):
    region = current_user.region
    if not region:
        raise HTTPException(status_code=404, detail="Region not found for user")
    question = await services.get_current_question_for_region(db, region)
    if not question:
        raise HTTPException(status_code=404, detail="No question available for this region")
    return question
