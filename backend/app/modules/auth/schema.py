from typing import Literal

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class UserRegisterSchema(BaseModel):
    full_name: str = Field(..., min_length=3, max_length=100)
    email: EmailStr
    password: str = Field(..., min_length=8)
    confirm_password: str = Field(..., min_length=8)
    role: Literal["job_seeker", "recruiter"] = "job_seeker"

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "full_name": "Adiveppa Mamadapur",
                "email": "adiveppa@example.com",
                "password": "Password@123",
                "confirm_password": "Password@123",
                "role": "job_seeker",
            }
        }
    )


class UserLoginSchema(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=8)