from pydantic import BaseModel

from app.schemas.base import BaseDBSchema


class UserCreate(BaseModel):
    username: str
    password: str


class UserDB(BaseDBSchema):
    username: str
