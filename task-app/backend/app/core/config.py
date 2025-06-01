from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    environment: str = "dev"
    database_url: str  # Pydantic подгружает из .env

    class Config:
        env_file = ".env"


settings = Settings()
