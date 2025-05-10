import os
from dotenv import load_dotenv

# Carrega variáveis do arquivo .env se existir
load_dotenv()

# Caminhos de pastas
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "dados")
MODELS_DIR = os.path.join(BASE_DIR, "modelos")

# Tokens e configurações
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "sua-chave-aqui")
DATABASE_FILE = os.path.join(BASE_DIR, "ia_motor.db")
DATABASE_URL = os.getenv("DATABASE_URL", f"sqlite:///{DATABASE_FILE}")

# Configurações gerais
DEFAULT_UF = "ES"
DEFAULT_TAX_REGIME = "Lucro Real"
EMBEDDING_MODEL = "text-embedding-ada-002"

# CNPJ de teste padrão para debug (pode ser desativado em prod)
DEFAULT_CNPJ = "12345678000100"


