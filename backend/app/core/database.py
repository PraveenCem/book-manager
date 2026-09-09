from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings

class Database:
    def __init__(self):
        self.client = AsyncIOMotorClient(settings.db_url)
        self.db = self.client[settings.db]

db = Database()