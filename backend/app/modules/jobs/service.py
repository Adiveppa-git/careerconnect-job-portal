from app.modules.jobs.model import JobModel
from app.modules.jobs.repository import (
    create_job,
    get_all_jobs,
    get_job_by_id,
)


async def create_job_service(job_data, recruiter_email: str):
    """
    Create a new job.
    """

    job = JobModel(
        **job_data.model_dump(),
        recruiter_email=recruiter_email,
    )

    job_id = await create_job(job.model_dump())

    return {
        "id": str(job_id),
        "message": "Job created successfully",
    }


async def get_all_jobs_service():
    """
    Return all active jobs.
    """
    return await get_all_jobs()


async def get_job_by_id_service(job_id: str):
    """
    Return one job.
    """
    return await get_job_by_id(job_id)