from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from ia_motor.config import DATABASE_URL

# Criação do engine SQLAlchemy
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
)

# Sessão para conexões com o banco
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base declarativa para os modelos
Base = declarative_base()
