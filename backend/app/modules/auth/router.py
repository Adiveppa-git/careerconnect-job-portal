from fastapi import APIRouter, Depends, HTTPException, status

from app.modules.auth.dependencies import get_current_user
from app.modules.auth.schema import UserLoginSchema, UserRegisterSchema
from app.modules.auth.service import login_user, register_user

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(user: UserRegisterSchema):
    """
    Register a new user.
    """
    try:
        return await register_user(user)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )


@router.post("/login")
async def login(user: UserLoginSchema):
    """
    Authenticate user and return JWT access token.
    """
    try:
        return await login_user(
            user.email,
            user.password,
        )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(e),
        )


@router.get("/me")
async def get_me(current_user=Depends(get_current_user)):
    """
    Get the currently authenticated user.
    """

    return {
        "id": str(current_user["_id"]),
        "full_name": current_user["full_name"],
        "email": current_user["email"],
        "role": current_user["role"],
    }