from app.modules.auth.jwt_handler import create_access_token
from app.modules.auth.model import UserModel
from app.modules.auth.repository import (
    create_user,
    get_user_by_email,
)
from app.modules.auth.schema import UserRegisterSchema
from app.utils.security import (
    hash_password,
    verify_password,
)


async def register_user(user: UserRegisterSchema):
    """
    Register a new user.
    """

    # Check passwords match
    if user.password != user.confirm_password:
        raise ValueError("Passwords do not match")

    # Check if email already exists
    existing_user = await get_user_by_email(user.email)

    if existing_user:
        raise ValueError("Email already registered")

    # Hash password
    hashed_password = hash_password(user.password)

    # Create user model
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


async def login_user(email: str, password: str):
    """
    Authenticate user and return JWT token.
    """

    # Find user
    user = await get_user_by_email(email)

    if not user:
        raise ValueError("Invalid email or password")

    # Verify password
    if not verify_password(password, user["password_hash"]):
        raise ValueError("Invalid email or password")

    # Create JWT token
    token = create_access_token(
        {
            "sub": user["email"],
            "role": user["role"],
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer",
    }