from fastapi import APIRouter

from app.core.security import get_password_hash
from app.models.user import User
from app.schemas.user import UserCreate, UserDB

router = APIRouter()


@router.post("/register", response_model=UserDB)
async def register_user(user_in: UserCreate):
    user = await User(
        username=user_in.username, password=get_password_hash(user_in.password)
    )

    await user.save()

    return user
