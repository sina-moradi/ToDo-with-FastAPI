from fastapi import FastAPI

from routers.users import router as user_router
from routers.todo import router as todo_router

app = FastAPI()

app.include_router(user_router, prefix='/users')
app.include_router(todo_router, prefix='/todo')
