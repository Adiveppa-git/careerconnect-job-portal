from datetime import datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict, EmailStr


class UserModel(BaseModel):
    full_name: str
    email: EmailStr
    password_hash: str
    role: Literal["job_seeker", "recruiter"]
    is_verified: bool = False
    is_active: bool = True
    profile_picture: str | None = None
    resume_url: str | None = None
    created_at: datetime = datetime.utcnow()
    updated_at: datetime = datetime.utcnow()

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
    )