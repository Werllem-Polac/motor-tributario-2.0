from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from ia_motor.rotas import empresas, analise_xml, pareceres, simulador, lote_analise, chat_tributario
from ia_motor.services.auto_estrategista import definir_estrategia

app = FastAPI(
    title="Motor Tributário 2.0",
    description="API Inteligente para análise, simulação e defesa tributária por CNPJ",
    version="2.0.0"
)

# CORS (pode ser refinado conforme o ambiente)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inclusão das rotas
app.include_router(empresas.router, prefix="/empresas", tags=["Empresas"])
app.include_router(analise_xml.router, prefix="/xml", tags=["Análise XML"])
app.include_router(pareceres.router, prefix="/pareceres", tags=["Pareceres Jurídicos"])
app.include_router(simulador.router, prefix="/simulador", tags=["Simulador Fiscal"])
app.include_router(lote_analise.router, prefix="/lote", tags=["Análise em Lote"])
app.include_router(chat_tributario.router, prefix="/chat", tags=["Chat Tributário"])

@app.get("/")
def root():
    return {"message": "Motor Tributário 2.0 rodando com sucesso"}

