from app.database.database import db

# MongoDB users collection
users_collection = db["users"]


async def get_user_by_email(email: str):
    """
    Find a user by email.
    """
    return await users_collection.find_one({"email": email})


async def create_user(user_data: dict):
    """
    Insert a new user into MongoDB.
    """
    result = await users_collection.insert_one(user_data)
    return result.inserted_id


async def get_user_by_id(user_id):
    """
    Find a user by MongoDB ObjectId.
    """
    return await users_collection.find_one({"_id": user_id})


async def update_user(user_id, update_data: dict):
    """
    Update a user's information.
    """
    result = await users_collection.update_one(
        {"_id": user_id},
        {"$set": update_data}
    )
    return result.modified_count


async def delete_user(user_id):
    """
    Delete a user.
    """
    result = await users_collection.delete_one({"_id": user_id})
    return result.deleted_count


async def get_all_users():
    """
    Get all users.
    """
    users = []
    async for user in users_collection.find():
        users.append(user)
    return users