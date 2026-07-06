from datetime import datetime, timezone

from pydantic import BaseModel, ConfigDict, Field


class JobModel(BaseModel):
    title: str
    company_name: str
    recruiter_email: str
    location: str
    employment_type: str
    experience_level: str
    salary: str
    skills: list[str]
    description: str
    application_deadline: datetime

    is_active: bool = True

    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
    )