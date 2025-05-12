# main.py na raiz do projeto
from app.api.main import app

# Isso garante que o Uvicorn ou qualquer outro servidor que rode "main:app"
# encontre a instância correta

