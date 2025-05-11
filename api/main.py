"""
Ponto de entrada principal da API FastAPI.
Configura middlewares, banco de dados e rotas usando configuração centralizada.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.database.session import engine, Base
from api.config import settings

# Importa e registra rotas modulares
from api.empresas.routes import router as empresas_router
# (adicione aqui outros routers conforme modularização)

# Instancia a aplicação
app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.API_VERSION
)

# Middleware de CORS (ajuste origens conforme necessário)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, especifique domínios permitidos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Criação automática das tabelas (use Alembic futuramente em produção)
Base.metadata.create_all(bind=engine)

# Registro das rotas
app.include_router(empresas_router)

