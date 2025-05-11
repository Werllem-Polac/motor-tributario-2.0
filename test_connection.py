from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from settings import DATABASE_URL  # ou from database.config import DATABASE_URL

print(f"🔎 DATABASE_URL: {DATABASE_URL}")

try:
    engine = create_engine(DATABASE_URL)
    with engine.connect() as conn:
        result = conn.execute("SELECT version();")
        version = result.fetchone()
        print(f"✅ Conectado com sucesso ao PostgreSQL! Versão: {version[0]}")
except OperationalError as e:
    print("❌ Erro ao conectar ao banco de dados:")
    print(e)
