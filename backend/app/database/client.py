from pymongo import AsyncMongoClient
from app.config.settings import settings

# Create a single MongoDB client for the application
client = AsyncMongoClient(settings.MONGODB_URL)