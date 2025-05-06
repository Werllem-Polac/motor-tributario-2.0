from sqlalchemy import Column, Integer, String, Float, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

class Empresa(Base):
    __tablename__ = "empresas"
    id = Column(Integer, primary_key=True)
    cnpj = Column(String, unique=True, index=True)
    razao_social = Column(String)
    produtos = relationship("Produto", back_populates="empresa")
    perguntas = relationship("PerguntaIA", back_populates="empresa")

class Produto(Base):
    __tablename__ = "produtos"
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    valor = Column(Float)
    empresa_id = Column(Integer, ForeignKey("empresas.id"))
    empresa = relationship("Empresa", back_populates="produtos")

class PerguntaIA(Base):
    __tablename__ = "perguntas"
    id = Column(Integer, primary_key=True)
    pergunta = Column(Text)
    resposta = Column(Text)
    cnpj = Column(String)
    criada_em = Column(DateTime, default=datetime.utcnow)
    empresa_id = Column(Integer, ForeignKey("empresas.id"))
    empresa = relationship("Empresa", back_populates="perguntas")
