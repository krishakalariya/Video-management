import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGO_DETAILS = os.getenv("MONGO_URL")

client = MongoClient(MONGO_DETAILS)
database = client.video_management
video_collection = database.get_collection("videos")

def video_helper(video) -> dict:
    return {
        "id": str(video["_id"]),
        "filename": video["filename"],
        "file_size": video["file_size"],
    }
