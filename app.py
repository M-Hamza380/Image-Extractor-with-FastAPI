from pathlib import Path
from fastapi import FastAPI, Request, Depends, File, UploadFile, HTTPException
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
from functools import lru_cache
import io, uuid, uvicorn

from src.ImageExtractor.config import Settings
from src.ImageExtractor.utils.common import ensure_make_dir

@lru_cache
def get_settings() -> Settings:
    return Settings()

Base_dir: Path = Path(__file__).parent
Upload_dir: Path = Base_dir / "static/Upload"
templates = Jinja2Templates(directory= str( Base_dir / "src/templates"))
app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home(request: Request, settings: Settings = Depends(get_settings)) -> HTMLResponse:
    """
    Home page endpoint.

    Returns a rendered HTMLResponse with the "home.html" template.

    Args:
    - request (Request): The request object.
    - settings (Settings): The app settings. Defaults to the result of `get_settings()`.

    Returns:
    - HTMLResponse: The rendered HTMLResponse.
    """
    return templates.TemplateResponse("home.html", {"request": request}) 

@app.post("/img-upload", response_class=FileResponse)
async def upload_img(request: Request, file: UploadFile = File(...), settings: Settings = Depends(get_settings)) -> FileResponse:
    """
    Upload image endpoint.

    Uploads the image from the request body and writes it to the "static/Upload" directory.

    Args:
    - request (Request): The request object.
    - file (UploadFile): The uploaded file.
    - settings (Settings): The app settings. Defaults to the result of `get_settings()`.

    Returns:
    - FileResponse: The uploaded file.
    """
    if not settings.echo_active:
        raise HTTPException(status_code=404, detail="Not found")
    
    ensure_make_dir(str(Upload_dir))
    byte_str = io.BytesIO(await file.read())
    fname = Path(file.filename)
    ext: str = fname.suffix
    new_name: str = str(uuid.uuid4()) + ext
    destination: Path = Upload_dir / new_name
    
    with open(destination, "wb") as f:
        f.write(byte_str.read())    
    return destination

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=7172)
