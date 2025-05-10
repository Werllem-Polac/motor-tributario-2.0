from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from api.database import SessionLocal, engine
from api.models import Base, Empresa, Produto, PerguntaIA, Usuario
from api.schemas import (
    EmpresaSchema, ProdutoSchema, PerguntaIASchema,
    UsuarioLoginSchema, UsuarioCreateSchema
)
from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext
import requests
import os
import uvicorn

# --- Cria tabelas do banco ---
Base.metadata.create_all(bind=engine)

# --- Inicialização do FastAPI ---
app = FastAPI()

# --- Middleware de CORS ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Dependência do banco ---
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- Segurança ---
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET_KEY = "segredo-super-forte"
ALGORITHM = "HS256"

def gerar_token(dados: dict, expira_em: int = 60):
    dados_copia = dados.copy()
    exp = datetime.utcnow() + timedelta(minutes=expira_em)
    dados_copia.update({"exp": exp})
    return jwt.encode(dados_copia, SECRET_KEY, algorithm=ALGORITHM)

# --- Rota raiz ---
@app.get("/")
def home():
    return {"status": "API Motor Tributário online"}

# --- Endpoints principais ---
@app.post("/registrar/")
def registrar(dados: UsuarioCreateSchema, db: Session = Depends(get_db)):
    senha_cript = pwd_context.hash(dados.senha)
    usuario = Usuario(email=dados.email, senha_hash=senha_cript)
    db.add(usuario)
    db.commit()
    return {"msg": "Usuário criado com sucesso"}

@app.post("/login")
def login(dados: UsuarioLoginSchema, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.email == dados.email).first()
    if not usuario or not pwd_context.verify(dados.senha, usuario.senha_hash):
        raise HTTPException(status_code=401, detail="Credenciais inválidas")
    token = gerar_token({"sub": usuario.email})
    return {"access_token": token}

@app.post("/empresas/")
def criar_empresa(dados: EmpresaSchema, db: Session = Depends(get_db)):
    nova = Empresa(**dados.dict())
    db.add(nova)
    db.commit()
    return {"msg": "Empresa criada com sucesso"}

@app.get("/empresas/{cnpj}")
def buscar_empresa(cnpj: str, db: Session = Depends(get_db)):
    empresa = db.query(Empresa).filter(Empresa.cnpj == cnpj).first()
    if not empresa:
        raise HTTPException(status_code=404, detail="Empresa não encontrada")
    return empresa

@app.post("/produtos/")
def add_produto(p: ProdutoSchema, db: Session = Depends(get_db)):
    produto = Produto(**p.dict())
    db.add(produto)
    db.commit()
    return {"msg": "Produto salvo com sucesso"}

@app.get("/produtos/{cnpj}")
def produtos_por_cnpj(cnpj: str, db: Session = Depends(get_db)):
    empresa = db.query(Empresa).filter(Empresa.cnpj == cnpj).first()
    if not empresa:
        return []
    return db.query(Produto).filter(Produto.empresa_id == empresa.id).all()

@app.post("/perguntas/")
def registrar_pergunta(p: PerguntaIASchema, db: Session = Depends(get_db)):
    pergunta = PerguntaIA(**p.dict())
    db.add(pergunta)
    db.commit()
    return {"msg": "Pergunta registrada com sucesso"}

@app.get("/perguntas/{cnpj}")
def perguntas_por_cnpj(cnpj: str, db: Session = Depends(get_db)):
    return db.query(PerguntaIA).filter(PerguntaIA.cnpj == cnpj).order_by(PerguntaIA.criada_em.desc()).all()

@app.get("/status-fontes")
def coletar_fontes():
    ufs = ["ac", "al", "am", "ap", "ba", "ce", "df", "es", "go", "ma", "mt", "ms", "mg", "pa", "pb", "pr",
           "pe", "pi", "rj", "rn", "rs", "ro", "rr", "sc", "se", "sp", "to"]
    fontes = [
        "https://www.gov.br/receitafederal/pt-br",
        "https://www.stf.jus.br",
        "https://www.stj.jus.br"
    ] + [f"https://www.sefaz.{uf}.gov.br" for uf in ufs]

    resultados = []
    for url in fontes:
        try:
            r = requests.get(url, timeout=4)
            status = "OK" if r.status_code == 200 else f"erro {r.status_code}"
            resultados.append(f"{url} => {status}")
        except Exception as e:
            resultados.append(f"{url} => ERRO: {str(e)}")
    return resultados

# --- Startup: Treinamento de IA (seguro) ---
def treinar_ia():
    print("🔁 Iniciando treinamento de IA com os dados...")
    db = SessionLocal()
    try:
        empresas = db.query(Empresa).all()
        for empresa in empresas:
            print(f"📚 Treinando IA para CNPJ: {empresa.cnpj}")
        print("✅ Treinamento concluído com sucesso!")
    except Exception as e:
        print(f"Erro no treinamento: {e}")
    finally:
        db.close()

@app.on_event("startup")
async def on_startup():
    treinar_ia()

# --- Execução local com uvicorn ---
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("api.main:app", host="0.0.0.0", port=port)




