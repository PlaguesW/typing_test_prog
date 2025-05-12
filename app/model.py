from sqlalchemy import Column, Integer, String, Text, ForeignKey, Float, DateTime
from sqlalchemy.sql import func
from .database import Base

class Text(Base):
    __tablename__ = "texts"
    id = Column(Integer, primary_key=True, index=True)
    language = Column(String, index=True)
    content = Column(Text)

class Result(Base):
    __tablename__ = "results"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String)
    language = Column(String)
    wpm = Column(Float)
    cpm = Column(Float)
    accuracy = Column(Float)
    errors = Column(Integer)
    timestamp = Column(DateTime, server_default=func.now())