from .user import User
from .todo import ToDo

from sqlalchemy.orm import relationship

User.todos = relationship("ToDo", back_populates='todos')
ToDo.owner = relationship("User", back_populates="owner")