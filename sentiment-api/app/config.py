# from pydantic import BaseSettings

# class Settings(BaseSettings):
#     DATABASE_URL: str
#     JWT_SECRET: str
#     JWT_ALGO: str = "HS256"
#     JWT_EXPIRE_MINUTES: int = 30
#     HF_API_KEY: str
#     FRONTEND_URL: str

#     class Config:
#         env_file = ".env"

# settings = Settings()
import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    HF_API_KEY: str = os.getenv("HF_API_KEY")
    JWT_SECRET: str = os.getenv("JWT_SECRET")
    BACKEND_URL: str = os.getenv("BACKEND_URL", "http://localhost:8000")
   # PostgreSQL
    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB")
    POSTGRES_HOST: str = os.getenv("POSTGRES_HOST", "localhost")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT", "5432")

    SQLALCHEMY_DATABASE_URL: str = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

settings = Settings()
