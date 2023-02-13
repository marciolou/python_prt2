from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base

class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    DB_URL: str = 'postgresql+asyncpg://teste:123456@192.168.0.53:5439/postgres'
    DB_BaseModel = declarative_base()

    class Config:
        case_sensitive = True
settings: Settings = Settings()
