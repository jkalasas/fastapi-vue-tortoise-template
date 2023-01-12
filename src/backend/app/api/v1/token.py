from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from app.core.auth import authenticate, create_access_token
from app.schemas.token import Token

router = APIRouter()


@router.post("/new", response_model=Token)
async def new_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await authenticate(form_data.username, form_data.password)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid credentials",
        )

    return {
        "access_token": create_access_token(sub=user.id),
        "token_type": "bearer",
    }
