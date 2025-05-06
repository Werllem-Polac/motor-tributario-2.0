from dotenv import load_dotenv
import os

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./uploads.db")
SECRET_KEY = os.getenv("SECRET_KEY", "troque_esta_chave_para_producao")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if OPENAI_API_KEY is None: raise RuntimeError("🔑 Defina OPENAI_API_KEY no .env!")
