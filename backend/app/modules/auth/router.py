from fastapi import APIRouter

from app.modules.auth.schema import UserRegisterSchema

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post("/register")
async def register(user: UserRegisterSchema):
    return {
        "message": "Validation Successful",
        "data": user,
    }