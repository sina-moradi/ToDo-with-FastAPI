from pydantic import BaseModel


class UserInput(BaseModel):
    username: str
    password: str


class UpdateInput(BaseModel):
    username: str


class RetrieveUser(BaseModel):
    username: str
    id: int


class Token(BaseModel):
    access_token: str
    token_type: str
