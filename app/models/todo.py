from .engine import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

from enum import Enum
from .user import User


class TodoStatusEnum(str, Enum):
    not_start = 'not started'
    priority = 'In priority to do'
    doing = 'doing'
    is_done = 'is_done'


class ToDo(Base):
    __tablename__ = 'ToDo'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    status: Mapped[TodoStatusEnum] = mapped_column(nullable=False)
    title: Mapped[str] = mapped_column(nullable=False)
    detail: Mapped[str] = mapped_column(nullable=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
