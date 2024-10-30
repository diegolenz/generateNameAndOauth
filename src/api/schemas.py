from pydantic import BaseModel, EmailStr


class Message(BaseModel):
    message: str


class GeneratedNameResponse():
    name: str
    id: str



class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    userName: str | None = None
