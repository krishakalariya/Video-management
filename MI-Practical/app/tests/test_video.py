from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_upload_video():
    with open("test_video.mp4", "rb") as video:
        response = client.post("/video/upload", files={"file": video})
        assert response.status_code == 200
        assert response.json() == {"message": "Video is being processed"}

def test_search_video():
    response = client.get("/video/search?filename=test_video.mp4")
    assert response.status_code == 200
    assert "filename" in response.json()[0]
