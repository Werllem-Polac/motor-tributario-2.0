from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from ia_motor.database.engine import Base

class Empresa(Base):
    __tablename__ = "empresas"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    cnpj = Column(String, unique=True, index=True)
    uf = Column(String, default="ES")
    regime = Column(String, default="Lucro Real")
    aceite_lgpd = Column(String, default="false")

    documentos = relationship("DocumentoFiscal", back_populates="empresa")
    analises = relationship("AnaliseFiscal", back_populates="empresa")

class DocumentoFiscal(Base):
    __tablename__ = "documentos_fiscais"

    id = Column(Integer, primary_key=True, index=True)
    empresa_id = Column(Integer, ForeignKey("empresas.id"))
    tipo = Column(String)  # SPED, XML, CSV, etc.
    nome_arquivo = Column(String)
    data_upload = Column(DateTime, default=datetime.utcnow)
    conteudo = Column(Text)  # opcional, ou usar caminho para o arquivo processado

    empresa = relationship("Empresa", back_populates="documentos")

class AnaliseFiscal(Base):
    __tablename__ = "analises_fiscais"

    id = Column(Integer, primary_key=True, index=True)
    empresa_id = Column(Integer, ForeignKey("empresas.id"))
    data_analise = Column(DateTime, default=datetime.utcnow)
    tese_sugerida = Column(String)
    economia_estimativa = Column(Float)
    risco_percentual = Column(Float)
    parecer = Column(Text)

    empresa = relationship("Empresa", back_populates="analises")

class Jurisprudencia(Base):
    __tablename__ = "jurisprudencias"

    id = Column(Integer, primary_key=True, index=True)
    tese = Column(String)
    orgao = Column(String)  # STF, STJ, SEFAZ, etc.
    ementa = Column(Text)
    link = Column(String)
    data_publicacao = Column(DateTime)

