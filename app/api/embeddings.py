from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.dialects.postgresql import ARRAY
from api.database.session import Base

class Embedding(Base):
    __tablename__ = "embeddings"

    id = Column(Integer, primary_key=True, index=True)
    fonte = Column(String, index=True)
    titulo = Column(String)
    vetor = Column(ARRAY(Float))  # Suporta vetor se o PostgreSQL usar extensão pgvector
