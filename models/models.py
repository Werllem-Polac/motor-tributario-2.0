from sqlalchemy import Column, String, Text, Enum, Boolean, Date, ForeignKey, ARRAY
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
ffrom app.api.database.session import Base

class CNAE(Base):
    __tablename__ = "cnaes"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    codigo_cnae = Column(String, unique=True, nullable=False)
    descricao = Column(Text, nullable=False)
    tipo_atividade = Column(Enum("Indústria", "Comércio", "Serviço", "Misto", name="tipoatividade"), nullable=False)

    beneficios = relationship("CNAEBeneficio", back_populates="cnae")
    jurisprudencias = relationship("CNAEJurisprudencia", back_populates="cnae")

class BeneficioFiscal(Base):
    __tablename__ = "beneficios_fiscais"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nome = Column(String, nullable=False)
    tipo = Column(Enum("Federal", "Estadual", "Setorial", name="tipobeneficio"), nullable=False)
    descricao = Column(Text)
    abrangencia_uf = Column(ARRAY(String))
    ativo = Column(Boolean, default=True)

    cnaes = relationship("CNAEBeneficio", back_populates="beneficio")

class CNAEBeneficio(Base):
    __tablename__ = "cnae_beneficios"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    cnae_id = Column(UUID(as_uuid=True), ForeignKey("cnaes.id"))
    beneficio_id = Column(UUID(as_uuid=True), ForeignKey("beneficios_fiscais.id"))

    cnae = relationship("CNAE", back_populates="beneficios")
    beneficio = relationship("BeneficioFiscal", back_populates="cnaes")

class Jurisprudencia(Base):
    __tablename__ = "jurisprudencias"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    titulo = Column(String, nullable=False)
    descricao = Column(Text)
    tribunal = Column(Enum("STF", "STJ", "TJ", "SEFAZ", "CARF", name="tribunais"), nullable=False)
    link_documento = Column(String)
    uf = Column(String)
    data_publicacao = Column(Date)

    cnaes = relationship("CNAEJurisprudencia", back_populates="jurisprudencia")

class CNAEJurisprudencia(Base):
    __tablename__ = "cnae_jurisprudencias"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    cnae_id = Column(UUID(as_uuid=True), ForeignKey("cnaes.id"))
    jurisprudencia_id = Column(UUID(as_uuid=True), ForeignKey("jurisprudencias.id"))

    cnae = relationship("CNAE", back_populates="jurisprudencias")
    jurisprudencia = relationship("Jurisprudencia", back_populates="cnaes")
