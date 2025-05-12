from app.api.database.session import Base, engine
import models.models  # garante o registro das tabelas

# Cria todas as tabelas definidas nos modelos
Base.metadata.create_all(bind=engine)

print("✅ Banco de dados inicializado com sucesso.")

