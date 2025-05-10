from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime

# ✅ Este é o Base necessário para o create_all funcionar
Base = declarative_base()

class Empresa(Base):
    __tablename__ = "empresas"

    id = Column(Integer, primary_key=True, index=True)
    razao_social = Column(String, nullable=False)
    cnpj = Column(String, unique=True, nullable=False)
    logradouro = Column(String)
    numero = Column(String)
    bairro = Column(String)
    cidade = Column(String)
    estado = Column(String)
    cep = Column(String)
    telefone = Column(String)
    email = Column(String)

    produtos = relationship("Produto", back_populates="empresa")

class Produto(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    ncm = Column(String)
    cfop = Column(String)
    cst = Column(String)
    valor = Column(String)
    empresa_id = Column(Integer, ForeignKey("empresas.id"))

    empresa = relationship("Empresa", back_populates="produtos")

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False)
    senha_hash = Column(String, nullable=False)

class PerguntaIA(Base):
    __tablename__ = "perguntas_ia"

    id = Column(Integer, primary_key=True, index=True)
    cnpj = Column(String, nullable=False)
    pergunta = Column(String, nullable=False)
    resposta = Column(String)
    criada_em = Column(DateTime, default=datetime.utcnow)
