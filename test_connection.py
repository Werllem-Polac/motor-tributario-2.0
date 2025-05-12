import sys
import io
from sqlalchemy import create_engine
from sqlalchemy.engine.url import make_url
from sqlalchemy.exc import OperationalError
from settings import DATABASE_URL

# Força saída UTF-8 no terminal
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

print(f"🔎 DATABASE_URL: {DATABASE_URL}")

try:
    url = make_url(DATABASE_URL)
    engine = create_engine(url, connect_args={"options": "-c client_encoding=utf8"})

    with engine.connect() as conn:
        result = conn.execute("SELECT version();")
        version = result.fetchone()
        print(f"✅ Conectado com sucesso ao PostgreSQL! Versão: {version[0]}")

except OperationalError as e:
    print("❌ Erro ao conectar ao banco de dados (OperationalError):")
    print(str(e).encode('utf-8', errors='replace').decode('utf-8', errors='replace'))

except Exception as e:
    print("❌ Erro inesperado:")
    print(str(e).encode('utf-8', errors='replace').decode('utf-8', errors='replace'))
