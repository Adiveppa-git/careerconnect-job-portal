from bson import ObjectId

from app.database.database import db

# MongoDB jobs collection
jobs_collection = db["jobs"]


async def create_job(job_data: dict):
    """
    Insert a new job into MongoDB.
    """
    result = await jobs_collection.insert_one(job_data)
    return result.inserted_id


async def get_all_jobs():
    """
    Return all active jobs.
    """
    jobs = []

    async for job in jobs_collection.find({"is_active": True}):
        job["_id"] = str(job["_id"])
        jobs.append(job)

    return jobs


async def get_job_by_id(job_id: str):
    """
    Find a job by its ID.
    """
    job = await jobs_collection.find_one(
        {
            "_id": ObjectId(job_id),
            "is_active": True,
        }
    )

    if job:
        job["_id"] = str(job["_id"])

    return job


async def update_job(job_id: str, update_data: dict):
    """
    Update an existing job.
    """
    result = await jobs_collection.update_one(
        {"_id": ObjectId(job_id)},
        {"$set": update_data},
    )

    return result.modified_count


async def delete_job(job_id: str):
    """
    Soft delete a job.
    """
    result = await jobs_collection.update_one(
        {"_id": ObjectId(job_id)},
        {
            "$set": {
                "is_active": False,
            }
        },
    )

    return result.modified_count