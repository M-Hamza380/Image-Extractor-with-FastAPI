from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv()

class Settings(BaseSettings):
    debug: bool = False
    echo_active: bool = False

    class Config:
        env_file: str = ".env"
        