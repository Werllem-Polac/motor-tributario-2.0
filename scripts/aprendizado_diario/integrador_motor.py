from sqlalchemy.orm import Session
from api.database.session import SessionLocal
# from api.models.embedding import Embedding  # Crie este modelo conforme seu banco

def salvar(vetores):
    """
    Salva os vetores jurídicos no motor de conhecimento (ex: banco PostgreSQL com pgvector).
    """
    db: Session = SessionLocal()
    for item in vetores:
        print(f"🔹 Salvando vetor: {item['titulo'][:60]}...")
        # db.add(Embedding(
        #     fonte=item["fonte"],
        #     titulo=item["titulo"],
        #     vetor=item["vetor"].tolist()
        # ))
    db.commit()
    db.close()
