# main.py
from fastapi import FastAPI
from .routes import video_routes

app = FastAPI()

app.include_router(video_routes.router, prefix="/video", tags=["video"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
