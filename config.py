# app/core/config.py
import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    API_AUTH_TOKEN: str = os.getenv("API_AUTH_TOKEN", "default_if_needed")
    DB_URL: str = os.getenv("DATABASE_URL")

settings = Settings()
