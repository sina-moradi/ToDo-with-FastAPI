from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.exceptions import ValidationException
from sqlalchemy.orm import Session

from models.engine import get_db
from schemas.users import RegisterInput
from models.user import User

router = APIRouter()


@router.post('/register')
def register(data: RegisterInput, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == data.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail='username is already exist')
    else:
        user = User(username=data.username, password=data.password)
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

