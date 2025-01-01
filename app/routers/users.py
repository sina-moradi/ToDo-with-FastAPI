from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.exceptions import ValidationException
from sqlalchemy.orm import Session

from models.engine import get_db
from schemas.users import RegisterInput, UpdateInput, RetrieveUser
from models.user import User
from utils.secret import pwd_context


router = APIRouter()


@router.post('/register', response_model=RetrieveUser)
def register(data: RegisterInput, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == data.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail='username is already exist')

    user_pass = pwd_context.hash(data.password)
    user = User(username=data.username, password=user_pass)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@router.put("/{user_id}", response_model=RetrieveUser)
def update_username(user_id: int, data: UpdateInput, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db_user.username = data.username
    db.commit()
    db.refresh(db_user)
    return db_user


@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return {"message": "User deleted"}