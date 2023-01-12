from datetime import datetime, timedelta
from typing import List, MutableMapping, Optional, Union

from fastapi.security import OAuth2PasswordBearer
from jose import jwt

from app.models.user import User
from app.core.config import settings
from app.core.security import verify_password

JWTPayloadMapping = MutableMapping[
    str, Union[datetime, bool, str, List[str], List[int]]
]

oauth2_scheme = OAuth2PasswordBearer(tokenUrl=settings.AUTH_ROUTE)


async def authenticate(username: str, password: str) -> Optional[User]:
    user = await User.filter(username=username).first()
    if user and verify_password(password, user.password):
        return user


def create_access_token(*, sub: str) -> str:
    return _create_token(
        token_type="access_token",
        lifetime=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),
        sub=sub,
    )


def _create_token(token_type: str, lifetime: timedelta, sub: str) -> str:
    payload = {
        "type": token_type,
        "exp": datetime.utcnow() + lifetime,
        "iat": datetime.utcnow(),
        "sub": str(sub),
    }

    return jwt.encode(payload, settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM)
