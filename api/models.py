from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    senha_hash = Column(String, nullable=False)

    empresas = relationship("Empresa", back_populates="dono")


class Empresa(Base):
    __tablename__ = "empresas"
    id = Column(Integer, primary_key=True, index=True)
    razao_social = Column(String, nullable=False)
    cnpj = Column(String, unique=True, index=True, nullable=False)
    dono_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    criado_em = Column(DateTime, default=datetime.utcnow)

    dono = relationship("Usuario", back_populates="empresas")
    produtos = relationship("Produto", back_populates="empresa")
    perguntas = relationship("PerguntaIA", back_populates="empresa")


class Produto(Base):
    __tablename__ = "produtos"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    valor = Column(Numeric(12, 2), nullable=False)
    empresa_id = Column(Integer, ForeignKey("empresas.id"))

    empresa = relationship("Empresa", back_populates="produtos")


class PerguntaIA(Base):
    __tablename__ = "perguntas"
    id = Column(Integer, primary_key=True, index=True)
    pergunta = Column(String, nullable=False)
    resposta = Column(String)
    cnpj = Column(String, nullable=False)
    criada_em = Column(DateTime, default=datetime.utcnow)
    empresa_id = Column(Integer, ForeignKey("empresas.id"))

    empresa = relationship("Empresa", back_populates="perguntas")
