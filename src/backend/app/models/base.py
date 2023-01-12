from tortoise.fields import DatetimeField, IntField


class BaseModel:
    id = IntField(pk=True, index=True)
    created_on = DatetimeField(auto_now_add=True)
    updated_on = DatetimeField(auto_now=True)

    def __repr__(self) -> str:
        return f"<{type(self).__name__} {self.id}>"

    def __str__(self) -> str:
        return self.__repr__()
