from datetime import datetime, timedelta, timezone
from fastapi import Depends, HTTPException, status
from dotenv import load_dotenv
from fastapi.security import OAuth2PasswordBearer
from jwt.exceptions import InvalidTokenError
import sqlalchemy as sa

import jwt
import os
from typing_extensions import Annotated

from models.engine import get_db
from models.user import User
from schemas.users import UpdateInput
from exceptions import UsernameOrPassIncorrect
from .secret import pwd_context

ACCESS_TOKEN_EXPIRE_MINUTES = 30
load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def authenticate_user(username: str, password: str, db):
    user = db.query(User).filter(User.username == username).first()
    if user is None:
        raise UsernameOrPassIncorrect
    if not pwd_context.verify(password, user.password):
        raise UsernameOrPassIncorrect
    return user


def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )


def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):

    try:
        print('execute')
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = UpdateInput(username=username)
    except InvalidTokenError:
        raise credentials_exception
    user = sa.select(User).where(User.username == token_data.username)
    if user is None:
        raise credentials_exception
    return user