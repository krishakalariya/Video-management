from pydantic import BaseModel


class Video(BaseModel):
    filename: str
    file_size: float


class VideoSchema(BaseModel):
    filename: str
    file_size: int
