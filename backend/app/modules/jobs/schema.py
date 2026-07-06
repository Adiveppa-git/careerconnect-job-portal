from datetime import datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


class JobCreateSchema(BaseModel):
    title: str = Field(..., min_length=3, max_length=100)
    company_name: str = Field(..., min_length=2, max_length=100)
    location: str
    employment_type: Literal[
        "Full-time",
        "Part-time",
        "Internship",
        "Contract",
        "Remote",
    ]
    experience_level: Literal[
        "Fresher",
        "Junior",
        "Mid-Level",
        "Senior",
    ]
    salary: str
    skills: list[str]
    description: str = Field(..., min_length=20)
    application_deadline: datetime

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "title": "Full Stack Developer",
                "company_name": "CareerConnect",
                "location": "Bangalore",
                "employment_type": "Full-time",
                "experience_level": "Fresher",
                "salary": "6-8 LPA",
                "skills": [
                    "React",
                    "FastAPI",
                    "MongoDB"
                ],
                "description": "Looking for a Full Stack Developer with React and FastAPI knowledge.",
                "application_deadline": "2026-08-31T23:59:59Z"
            }
        }
    )