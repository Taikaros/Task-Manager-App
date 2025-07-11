# app/schemas.py
from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    username: str
    password: str

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None

class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None

    class Config:
        orm_mode = True

class UserResponse(BaseModel):
    username: str