# app/auth.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from . import models 
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_user(db: Session, username: str, password: str):
    hashed_password = pwd_context.hash(password)  # Hasheando la contraseña
    new_user = models.UserModel(username=username, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)