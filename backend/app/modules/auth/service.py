from app.modules.auth.repository import (
    get_user_by_email,
    create_user,
)
from app.modules.auth.model import UserModel
from app.modules.auth.schema import UserRegisterSchema
from app.utils.security import hash_password


async def register_user(user: UserRegisterSchema):
    # Check passwords match
    if user.password != user.confirm_password:
        raise ValueError("Passwords do not match")

    # Check email already exists
    existing_user = await get_user_by_email(user.email)

    if existing_user:
        raise ValueError("Email already registered")

    # Hash password
    hashed_password = hash_password(user.password)

    # Create database model
    new_user = UserModel(
        full_name=user.full_name,
        email=user.email,
        password_hash=hashed_password,
        role=user.role,
    )

    # Save user
    user_id = await create_user(new_user.model_dump())

    return {
        "id": str(user_id),
        "message": "User registered successfully",
    }