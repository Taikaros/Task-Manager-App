# app/models.py
from sqlalchemy import Column, Integer, String
from .database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class UserModel(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)  # <-- Asegúrate que sea 255 o más

class TaskModel(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String, nullable=True)
    owner_id = Column(Integer, ForeignKey('users.id'))

    owner = relationship("UserModel", back_populates="tasks")

UserModel.tasks = relationship("TaskModel", back_populates="owner")