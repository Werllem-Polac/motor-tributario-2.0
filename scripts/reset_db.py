import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from api.database import Base, engine

db_path = os.path.join(os.path.dirname(__file__), "..", "ia_motor", "ia_motor.db")
db_path = os.path.abspath(db_path)

if os.path.exists(db_path):
    os.remove(db_path)
    print("🗑️ Banco de dados antigo removido.")
else:
    print("⚠️ Nenhum banco de dados anterior encontrado.")

# Criação das tabelas
Base.metadata.create_all(bind=engine)
print("✅ Novo banco de dados criado com sucesso.")
