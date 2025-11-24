from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # Это самая важная часть:
    model_config = SettingsConfigDict(
        env_file=".env",             # Имя файла
        env_file_encoding="utf-8",   # Кодировка
        extra="ignore"               # Игнорировать лишние переменные
    )

settings = Settings()