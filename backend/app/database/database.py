from app.database.client import client
from app.config.settings import settings

# Reference to the application database
db = client[settings.DATABASE_NAME]