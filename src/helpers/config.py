from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):

    FILE_ALLOWED_TYPES : list
    FILE_MAX_SIZE: int
    APP_NAME: str
    APP_VERSION: str
    OPEN_API_KEY: str

    class Config:
        env_file = ".env"


def get_settings():
    return Settings()