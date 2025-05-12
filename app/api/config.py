"""
Carrega e centraliza as configurações da aplicação a partir de variáveis de ambiente.
"""

import os
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()

class Settings:
    PROJECT_NAME: str = os.getenv("PROJECT_NAME", "Motor Tributário API")
    API_VERSION: str = os.getenv("API_VERSION", "v1")

    DB_USER: str = os.getenv("DB_USER")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD")
    DB_HOST: str = os.getenv("DB_HOST", "localhost")
    DB_PORT: str = os.getenv("DB_PORT", "5432")
    DB_NAME: str = os.getenv("DB_NAME")

    @property
    def DATABASE_URL(self):
        return f"postgresql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    SECRET_KEY: str = os.getenv("SECRET_KEY", "dev_key")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  # 24h

settings = Settings()
