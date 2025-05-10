from ia_motor.database.engine import Base, engine
from ia_motor.database import models

# Cria todas as tabelas definidas em models.py
Base.metadata.create_all(bind=engine)

print(" Banco de dados inicializado com sucesso.")
