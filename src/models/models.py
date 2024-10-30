import json
from datetime import datetime
from pydantic import BaseModel, EmailStr

class User:
    def toJSON(self):
        return json.dumps(
            self,
            ensure_ascii = False,
            default = json_default
        ).encode('utf-8')
    def __init__(self, id, password,  email, userName, createdAt):
        self.email = email
        self.userName = userName
        self.password = password
        self.id = id,
        self.createdAt = createdAt
    id: int
    userName: str
    password: str
    email: str
    createdAt: datetime

def json_default(value):
    print(value)
    if isinstance(value, datetime):
        return dict(year=value.year, month=value.month, day=value.day)
    else:
        return value.__dict__


class UserPublic(BaseModel):
    id: int
    username: str
    email: EmailStr

class CreateUserRequestDto(BaseModel):
    def toJSON(self):
        return json.dumps(
            self,
            ensure_ascii=False,
            default=json_default
        ).encode('utf-8')
    userName: str
    email: EmailStr
    password: str

def fake_decode_token(token):
    return User(
        userName=token + "fakedecoded", email="john@example.com", full_name="John Doe"
    )

class TokenData():
    userName: str | None = None


class Token(BaseModel):
    access_token: str
    token_type: str
