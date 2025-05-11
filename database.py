from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# 🔄 Carrega variáveis do arquivo .env
load_dotenv()

# 🔧 URL de conexão com o banco (usando Railway)
DATABASE_URL = os.getenv("DATABASE_URL")

# 🚀 Cria a engine de conexão com o banco de dados
engine = create_engine(DATABASE_URL)

# 🧠 Cria a sessão de banco de dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 🧱 Base para todos os modelos do SQLAlchemy
Base = declarative_base()

# 🔁 Dependência para injeção de sessão nas rotas FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
