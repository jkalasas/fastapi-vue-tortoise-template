import logging
import pathlib
import sys
from typing import List, Optional, Union

from dotenv import load_dotenv
from loguru import logger
from pydantic import BaseSettings, validator

from app.core.logging import InterceptHandler

load_dotenv()

ROOT = pathlib.Path(__file__).resolve().parent.parent


class DBSettings(BaseSettings):
    DATABASE_URI: str = "sqlite://example.db"


class LoggingSettings(BaseSettings):
    LOGGING_LEVEL: int = logging.INFO

    USE_LOG_FILE: bool = False
    LOG_FILE_PATH: str = str(ROOT.parent)
    LOG_FILE_FORMAT: str = "app-{time}.log"
    ROTATION_TIME: str = "1 week"
    RETENTION_TIME: str = "1 month"


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

    AUTH_ROUTE: str = "/api/v1/token/new"
    JWT_SECRET: str = "PLEASE_CHANGE_THIS"
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    db = DBSettings()
    logging = LoggingSettings()

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


def setup_app_logging(config: Settings) -> None:
    """Prepare custom logging for our application."""
    LOGGERS = ("uvicorn.asgi", "uvicorn.access")
    logging.getLogger().handlers = [InterceptHandler()]
    for logger_name in LOGGERS:
        logging_logger = logging.getLogger(logger_name)
        logging_logger.handlers = [InterceptHandler(level=config.logging.LOGGING_LEVEL)]

    logger.configure(
        handlers=[{"sink": sys.stderr, "level": config.logging.LOGGING_LEVEL}]
    )
    if config.logging.USE_LOG_FILE:
        logger.add(
            f"{config.logging.LOG_FILE_PATH}/{config.logging.LOG_FILE_FORMAT}",
            rotation=config.logging.ROTATION_TIME,
            retention=config.logging.RETENTION_TIME,
        )


settings = Settings()
