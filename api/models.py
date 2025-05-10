from api.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    senha_hash = Column(String)
    aceite_lgpd = Column(Boolean, default=False)

class Empresa(Base):
    __tablename__ = "empresas"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    cnpj = Column(String, unique=True)
    produtos = relationship("Produto", back_populates="empresa")

class Produto(Base):
    __tablename__ = "produtos"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    ncm = Column(String)
    empresa_id = Column(Integer, ForeignKey("empresas.id"))
    empresa = relationship("Empresa", back_populates="produtos")

class PerguntaIA(Base):
    __tablename__ = "perguntas"
    id = Column(Integer, primary_key=True, index=True)
    pergunta = Column(String)
    cnpj = Column(String)
    criada_em = Column(DateTime, default=datetime.utcnow)

