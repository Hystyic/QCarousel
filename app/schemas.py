from typing import Optional
from datetime import datetime
from pydantic import BaseModel, ConfigDict

class QuestionBase(BaseModel):
    content: str

class QuestionCreate(QuestionBase):
    position_in_cycle: int

class Question(QuestionBase):
    id: int
    content: str

    model_config = ConfigDict(from_attributes=True)

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str
    region_id: int

class User(UserBase):
    id: int
    region_id: int
    content: str

    model_config = ConfigDict(from_attributes=True)

class Token(BaseModel):
    access_token: str
    token_type: str
