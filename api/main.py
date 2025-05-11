"""
Ponto de entrada principal da API FastAPI.
Responsável por configurar middlewares, conectar banco de dados e registrar rotas.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.database.session import engine, Base
from api.empresas import routes as empresas_routes

app = FastAPI()

# Middleware de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Criação automática das tabelas (migrations recomendadas futuramente)
Base.metadata.create_all(bind=engine)

# Registro de rotas
app.include_router(empresas_routes.router)
