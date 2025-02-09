import shutil, time
from fastapi.testclient import TestClient

from app import app, Base_dir



client = TestClient(app)

def test_get_home():
    response = client.get("/")
    assert response.text != "<h1>Hello, World!</h1>"
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]

def test_upload_img():
    img_saved_path = Base_dir / "static/Images"

    for path in img_saved_path.glob("*"):
        response = client.post("/img-upload", files={"file": open(path, "rb")})
        assert response.status_code == 200

