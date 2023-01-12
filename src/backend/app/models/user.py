from tortoise.fields import CharField, TextField
from tortoise.models import Model
from tortoise.validators import MinLengthValidator

from app.models.base import BaseModel


class User(BaseModel, Model):
    username = CharField(
        32, index=True, unique=True, validators=[MinLengthValidator(8)]
    )
    password = TextField()
