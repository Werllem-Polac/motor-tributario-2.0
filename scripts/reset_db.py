# scripts/reset_db.py

import sys
import os
from sqlalchemy.exc import SQLAlchemyError

# Garante que a raiz do projeto esteja no sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.api.database.session import Base, engine
import models.models  # Garante que todos os modelos sejam importados e registrados

def reset_db():
    print("🗑️ Resetando o banco de dados PostgreSQL...")

    try:
        Base.metadata.drop_all(bind=engine)
        print("🧨 Tabelas antigas removidas.")
    except Exception as e:
        print(f"❌ Erro ao remover tabelas: {e}")
        return

    try:
        Base.metadata.create_all(bind=engine)
        print("✅ Banco recriado com sucesso.")
    except SQLAlchemyError as e:
        print(f"❌ Erro ao criar tabelas: {e}")

if __name__ == "__main__":
    reset_db()

