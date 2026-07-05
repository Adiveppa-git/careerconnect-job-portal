from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config.settings import settings
from app.routers import health

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="CareerConnect Job Portal API",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router)


@app.get("/")
async def root():
    return {
        "message": "Welcome to CareerConnect API"
    }