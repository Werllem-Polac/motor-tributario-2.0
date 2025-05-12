from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.database.session import engine, Base
from api.routes import ia_juridica  # ou outras rotas

app = FastAPI(
    title="Motor Tributário Inteligente",
    version="1.0.0",
    description="API do sistema de inteligência fiscal e jurídica com análise por embeddings e analogia tributária."
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Criação automática das tabelas
Base.metadata.create_all(bind=engine)

# Rotas
app.include_router(ia_juridica.router)

@app.get("/")
def raiz():
    return {"mensagem": "Motor Tributário Inteligente ativo com IA Jurídica"}
