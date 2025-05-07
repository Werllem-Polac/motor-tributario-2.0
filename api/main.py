from fastapi import FastAPI, Depends, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base, Empresa, Produto, PerguntaIA
import os
import requests
from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext
from entrada_dados.leitor_csv import ler_arquivo_csv

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Dependência ---
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

@app.post("/registrar/")
def registrar(dados: dict, db: Session = Depends(get_db)):
    senha_cript = pwd_context.hash(dados["senha"])
    usuario = Usuario(email=dados["email"], senha_hash=senha_cript)
    db.add(usuario)
    db.commit()
    return {"msg": "Usuario criado com sucesso"}

@app.post("/login")
def login(dados: dict, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.email == dados["email"]).first()
    if not usuario or not pwd_context.verify(dados["senha"], usuario.senha_hash):
        raise HTTPException(status_code=401, detail="Credenciais inválidas")
    token = gerar_token({"sub": usuario.email})
    return {"access_token": token}

@app.post("/empresas/")
async def criar_empresa(empresa: EmpresaSchema):
    empresa = Empresa(**dados)
    db.add(empresa)
    db.commit()
    return {"msg": "Empresa criada"}

@app.get("/empresas/{cnpj}")
def buscar_empresa(cnpj: str, db: Session = Depends(get_db)):
    return db.query(Empresa).filter(Empresa.cnpj == cnpj).first()

@app.post("/produtos/")
def add_produto(p: dict, db: Session = Depends(get_db)):
    produto = Produto(**p)
    db.add(produto)
    db.commit()
    return {"msg": "Produto salvo"}

@app.get("/produtos/{cnpj}")
def produtos_por_cnpj(cnpj: str, db: Session = Depends(get_db)):
    empresa = db.query(Empresa).filter(Empresa.cnpj == cnpj).first()
    return db.query(Produto).filter(Produto.empresa_id == empresa.id).all() if empresa else []

@app.post("/perguntas/")
def registrar_pergunta(p: dict, db: Session = Depends(get_db)):
    pergunta = PerguntaIA(**p)
    db.add(pergunta)
    db.commit()
    return {"msg": "Pergunta registrada"}

@app.get("/perguntas/{cnpj}")
def perguntas_por_cnpj(cnpj: str, db: Session = Depends(get_db)):
    return db.query(PerguntaIA).filter(PerguntaIA.cnpj == cnpj).order_by(PerguntaIA.criada_em.desc()).all()

@app.get("/status-fontes")
def coletar_fontes():
    ufs = ["ac","al","am","ap","ba","ce","df","es","go","ma","mt","ms","mg","pa","pb","pr",
           "pe","pi","rj","rn","rs","ro","rr","sc","se","sp","to"]
    fontes = [
        "https://www.gov.br/receitafederal/pt-br", "https://www.stf.jus.br", "https://www.stj.jus.br"
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
