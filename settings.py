import os
from urllib.parse import quote_plus
from dotenv import load_dotenv

# Carrega o .env da raiz
dotenv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".env"))
if not os.path.exists(dotenv_path):
    dotenv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".env"))
load_dotenv(dotenv_path)

# Utilitários
def get_env_quoted(key: str) -> str:
    val = os.getenv(key)
    if val is None or val.strip() == "":
        raise RuntimeError(f"Variável obrigatória ausente: {key}")
    return quote_plus(val)

def get_env(key: str, default="") -> str:
    val = os.getenv(key, default)
    if val.strip() == "":
        raise RuntimeError(f"Variável {key} está vazia ou ausente.")
    return val

# Banco de Dados
POSTGRES_USER = get_env("POSTGRES_USER")
POSTGRES_PASSWORD = get_env_quoted("POSTGRES_PASSWORD")
POSTGRES_HOST = get_env("POSTGRES_HOST")
POSTGRES_PORT = get_env("POSTGRES_PORT")
POSTGRES_DB = get_env("POSTGRES_DB")

DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

# Segurança
SECRET_KEY = get_env("SECRET_KEY")
OPENAI_API_KEY = get_env("OPENAI_API_KEY")


