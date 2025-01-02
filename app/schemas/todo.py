from pydantic import BaseModel
from models.todo import TodoStatusEnum
from typing import Optional


class AddTodoInp(BaseModel):
    title: str
    status: TodoStatusEnum
    detail: Optional[str]
