from fastapi import APIRouter, Depends

from app.core.security import get_password_hash
from app.models.user import User
from app.schemas.user import UserCreate, UserDB
from app.api.deps.auth import get_current_user

router = APIRouter()


@router.post("/register", response_model=UserDB)
async def register_user(user_in: UserCreate):
    user = await User(
        username=user_in.username, password=get_password_hash(user_in.password)
    )

    await user.save()

    return user


@router.get("/me", response_model=UserDB)
async def get_current_user(user: User = Depends(get_current_user)):
    return user
