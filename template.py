import os, logging
from pathlib import Path
from typing import List

logging.basicConfig(
    level=logging.INFO,
    format="[ [%(asctime)s] : %(name)s  %(levelname)s : %(pathname)s : %(module)s : %(message)s ]"
)

Project_Name: str = "ImageExtractor"

list_of_files: List[str] = [
    f"src/{Project_Name}/users/errors/__init__.py",
    f"src/{Project_Name}/users/errors/handlers.py",
    f"src/{Project_Name}/users/main/__init__.py",
    f"src/{Project_Name}/users/main/routes.py",
    f"src/{Project_Name}/users/upload/__init__.py",
    f"src/{Project_Name}/users/upload/forms.py",
    f"src/{Project_Name}/users/upload/routes.py",
    f"src/{Project_Name}/static/main.css",
    f"src/{Project_Name}/templates/error/404.html",
    f"src/{Project_Name}/templates/home.html",
    f"src/{Project_Name}/templates/layout.html",
    f"src/{Project_Name}/templates/login.html",
    f"src/{Project_Name}/templates/post.html",
    f"src/{Project_Name}/templates/register.html",
    f"src/{Project_Name}/templates/reset_request.html",
    f"src/{Project_Name}/templates/reset_token.html",
    f"src/{Project_Name}/templates/users_posts.html",
    f"src/{Project_Name}/views/__init__.py",
    f"src/{Project_Name}/views/views.py",
    f"src/{Project_Name}/utils/__init__.py",
    f"src/{Project_Name}/utils/logger.py",
    f"src/{Project_Name}/utils/exception.py",
    f"src/{Project_Name}/utils/common.py",
    ".env",
    ".env.example",
    "Makefile",
    "requirements.txt",
    "app.py"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} is already exists")
