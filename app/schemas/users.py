from pydantic import BaseModel
from typing import List


class UserInput(BaseModel):
    username: str
    password: str


class UpdateInput(BaseModel):
    username: str


class Users(BaseModel):
    id: int
    username: str


class UserList(BaseModel):
    users: List[Users]


class RetrieveUser(BaseModel):
    username: str
    id: int

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str
