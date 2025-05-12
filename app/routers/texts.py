from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from .. import models
import random

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/texts/random")
def get_random_text(lang: str, db: Session = Depends(get_db)):
    texts = db.query(models.Text).filter(models.Text.language == lang).all()
    return random.choice(texts) if texts else {"error": "No texts found"}