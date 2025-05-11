import os
from urllib.parse import quote_plus
from dotenv import load_dotenv

# Carrega variáveis do .env
load_dotenv()

# Variáveis de ambiente
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = quote_plus(os.getenv("POSTGRES_PASSWORD"))  # codifica *
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")
POSTGRES_DB = os.getenv("POSTGRES_DB")

# Monta a URL de conexão
DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

# Segurança
SECRET_KEY = os.getenv("SECRET_KEY", "troque_esta_chave_para_producao")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if OPENAI_API_KEY is None:
    raise RuntimeError("🔑 Defina OPENAI_API_KEY no .env!")
