import os
from typing import Optional

import aiofiles
from fastapi import APIRouter, UploadFile, File, HTTPException, BackgroundTasks

from ..database import video_collection
from moviepy.editor import VideoFileClip

router = APIRouter()

UPLOAD_FOLDER = "./uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def convert_to_mp4(input_file, output_file):
    try:
        video = VideoFileClip(input_file)
        video.write_videofile(output_file, codec='libx264', audio_codec='aac')
        video.close()
    except Exception as e:
        print(f"Error converting video: {e}")
        raise


@router.post("/upload")
async def upload(file: UploadFile = File(...)):
    try:
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        async with aiofiles.open(file_path, 'wb') as f:
            await f.write(await file.read())


        video_metadata = {"filename": file.filename, "file_size": file.size}
        video_collection.insert_one(video_metadata)

        return {"message": "Upload successful", "filename": file.filename}

    except Exception as e:
        return {"error": str(e)}


@router.get("/search")
async def search(filename: Optional[str] = None, file_size: Optional[float] = None):
    query = {}
    if filename:
        query["filename"] = filename
    if file_size:
        query["file_size"] = file_size

    results = list(video_collection.find(query, {"_id": 0}))

    if not results:
        raise HTTPException(status_code=404, detail="No matching videos found")

    return results
