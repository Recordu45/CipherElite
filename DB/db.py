import motor.motor_asyncio
import os

MONGO_URI = os.getenv("MONGO_URI")

if not MONGO_URI:
    raise Exception("MONGO_URI is missing. Add it in Render Environment Variables.")

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
db = client["CipherElite"]
