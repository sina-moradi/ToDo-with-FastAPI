from pydantic import BaseModel


class RegisterInput(BaseModel):
    username: str
    password: str


class UpdateInput(BaseModel):
    username: str


class RetrieveUser(BaseModel):
    username: str
    id: int