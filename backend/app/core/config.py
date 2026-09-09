from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    db_url: str
    db: str

    class Config:
        env_file = ".env"

settings = Settings()