from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.session import get_db
router = APIRouter()
@router.post("/register")
def register():
    return {"message": "User registered"}
@router.post("/login")
def login():
    return {"access_token": "token", "token_type": "bearer"}
