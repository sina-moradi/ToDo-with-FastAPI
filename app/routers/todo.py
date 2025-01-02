from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from models import ToDo, User
from models.engine import get_db
from schemas.todo import AddTodoInp
from utils.jwt_handle import get_current_user
router = APIRouter()


@router.post('/add')
def add_todo(data: AddTodoInp, db: Session = Depends(get_db),
             current_user: User = Depends(get_current_user)):
    todo = ToDo(title=data.title, status=data.status, detail=data.detail, user_id=current_user.id)
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo