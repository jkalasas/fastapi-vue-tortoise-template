from datetime import datetime

from pydantic import BaseModel


class BaseDBSchema(BaseModel):
    id: int
    created_on: datetime
    updated_on: datetime

    class Config:
        orm_mode = True
