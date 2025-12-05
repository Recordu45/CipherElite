from motor.motor_asyncio import AsyncIOMotorClient
import os

MONGO_URI = os.getenv("MONGO_URI")

if not MONGO_URI:
    raise Exception("MONGO_URI is missing. Add it in Render Environment Variables.")

client = AsyncIOMotorClient(MONGO_URI)
db = client["CipherElite"]
