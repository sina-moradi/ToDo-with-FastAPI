from fastapi import HTTPException


class UsernameOrPassIncorrect(HTTPException):
    def __init__(self):
        self.status_code = 400
        self.detail = "username or password is incorrect"
