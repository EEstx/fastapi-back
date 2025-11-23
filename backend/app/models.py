from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)

class Group(Base):
    __tablename__ = "groups"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String) # Например "Гвозди 50мм"
    # Характеристики, объединяющие эту группу
    common_features = Column(JSONB, default={}) 
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    items = relationship("STE", back_populates="group")

class STE(Base):
    __tablename__ = "stes"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    # Сырые характеристики: {"длина": "50мм", "материал": "сталь", "цвет": "серый"}
    features = Column(JSONB, nullable=False) 
    
    group_id = Column(Integer, ForeignKey("groups.id"), nullable=True)
    group = relationship("Group", back_populates="items")