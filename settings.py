import os
from urllib.parse import quote_plus
from dotenv import load_dotenv

# Força o carregamento do .env na raiz do projeto
dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
if not os.path.exists(dotenv_path):
    dotenv_path = os.path.join(os.path.dirname(__file__), "..", ".env")

load_dotenv(dotenv_path=dotenv_path)

# Utilitário seguro para carregar e codificar variáveis obrigatórias
def get_env_quoted(key: str) -> str:
    value = os.getenv(key)
    if value is None or value.strip() == "":
        raise RuntimeError(f"❌ A variável {key} está ausente no .env ou está vazia.")
    return quote_plus(value)

def get_env(key: str, default: str = "") -> str:
    value = os.getenv(key, default)
    if value.strip() == "":
        raise RuntimeError(f"❌ A variável {key} está vazia no .env.")
    return value

# Banco de dados
POSTGRES_USER = get_env("POSTGRES_USER")
POSTGRES_PASSWORD = get_env_quoted("POSTGRES_PASSWORD")  # codifica *
POSTGRES_HOST = get_env("POSTGRES_HOST")
POSTGRES_PORT = get_env("POSTGRES_PORT")
POSTGRES_DB = get_env("POSTGRES_DB")

DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

# Segurança
SECRET_KEY = get_env("SECRET_KEY")
OPENAI_API_KEY = get_env("OPENAI_API_KEY")
