from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ResultCreate(BaseModel):
    user_id: str
    language: str
    wpm: float
    cpm: float
    accuracy: float
    errors: int

class ResultOut(ResultCreate):
    id: int
    timestamp: datetime

    class Config:
        orm_mode = True


class TextOut(BaseModel):
    id: int
    language: str
    content: str

    class Config:
        orm_mode = True