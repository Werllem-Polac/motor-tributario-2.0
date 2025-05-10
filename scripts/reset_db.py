# scripts/reset_db.py

import sys
import os
from sqlalchemy.exc import SQLAlchemyError

# Garante que o diretório raiz esteja no path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from ia_motor.database.engine import Base, engine
from ia_motor.database import models  # Garante que todas as tabelas sejam registradas

DB_PATH = "./ia_motor.db"

def reset_db():
    print("🗑️ Resetando banco de dados...")

    # Apagar o banco antigo se existir
    if os.path.exists(DB_PATH):
        try:
            Base.metadata.drop_all(bind=engine)
            print(f"🧨 Banco antigo removido: {DB_PATH}")
        except Exception as e:
            print(f"❌ Erro ao remover banco: {e}")
            return

    # Criar novamente as tabelas
    try:
        Base.metadata.create_all(bind=engine)
        print("✅ Banco recriado com sucesso.")
    except SQLAlchemyError as e:
        print(f"❌ Erro ao criar banco: {e}")

if __name__ == "__main__":
    reset_db()
