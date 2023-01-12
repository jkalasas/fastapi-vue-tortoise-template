from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise

from app.core.config import settings, setup_app_logging

setup_app_logging(settings)
app = FastAPI(title="Template API")

if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_origin_regex=settings.BACKEND_CORS_ORIGIN_REGEX,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

register_tortoise(
    app,
    db_url=settings.db.DATABASE_URI,
    modules={
        "models": [
            "app.models.user",
        ]
    },
    generate_schemas=True,
    add_exception_handlers=True,
)


@app.get("/")
def index():
    return {"hello": "world"}
