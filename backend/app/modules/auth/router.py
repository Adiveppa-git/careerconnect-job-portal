from fastapi import APIRouter, HTTPException

from app.modules.auth.schema import UserRegisterSchema
from app.modules.auth.service import register_user

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post("/register")
async def register(user: UserRegisterSchema):
    try:
        return await register_user(user)
    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e),
        )