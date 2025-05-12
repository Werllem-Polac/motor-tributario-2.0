from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text, Float, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from app.api.database.session import Base  # ✅ Corrigido

class Empresa(Base):
    __tablename__ = "empresas"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    cnpj = Column(String, unique=True, index=True, nullable=False)
    uf = Column(String, default="ES", nullable=False)
    regime = Column(String, default="Lucro Real", nullable=False)
    aceite_lgpd = Column(Boolean, default=False)

    documentos = relationship("DocumentoFiscal", back_populates="empresa")
    analises = relationship("AnaliseFiscal", back_populates="empresa")

class DocumentoFiscal(Base):
    __tablename__ = "documentos_fiscais"

    id = Column(Integer, primary_key=True, index=True)
    empresa_id = Column(Integer, ForeignKey("empresas.id"), nullable=False, index=True)
    tipo = Column(String, nullable=False)  # SPED, XML, CSV, etc.
    nome_arquivo = Column(String, nullable=False)
    data_upload = Column(DateTime, default=datetime.utcnow)
    conteudo = Column(Text)

    empresa = relationship("Empresa", back_populates="documentos")

class AnaliseFiscal(Base):
    __tablename__ = "analises_fiscais"

    id = Column(Integer, primary_key=True, index=True)
    empresa_id = Column(Integer, ForeignKey("empresas.id"), nullable=False, index=True)
    data_analise = Column(DateTime, default=datetime.utcnow)
    tese_sugerida = Column(String)
    economia_estimativa = Column(Float)
    risco_percentual = Column(Float)
    parecer = Column(Text)

    empresa = relationship("Empresa", back_populates="analises")

class Jurisprudencia(Base):
    __tablename__ = "jurisprudencias"

    id = Column(Integer, primary_key=True, index=True)
    tese = Column(String, nullable=False)
    orgao = Column(String, nullable=False)  # STF, STJ, SEFAZ, etc.
    ementa = Column(Text, nullable=False)
    link = Column(String)
    data_publicacao = Column(DateTime)


