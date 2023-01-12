from typing import List, Optional, Union

from pydantic import BaseSettings, validator


class Settings(BaseSettings):
    PRODUCTION_ENV: bool = False
    API_V1_STR: str = "/api/v1"

    BACKEND_HOST: str = "0.0.0.0"
    BACKEND_PORT: Union[str, int] = 8000

    BACKEND_CORS_ORIGINS: List[str] = [
        "http://localhost:8000",
        "http://127.0.0.1:8000",
    ]
    BACKEND_CORS_ORIGIN_REGEX: Optional[str] = "https.*\.(netlify.app|herokuapp.com)"

    @validator("BACKEND_CORS_ORIGINS")
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    class Config:
        case_sensitive = True
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
