import csv
from sqlalchemy.orm import Session
from models.models import Jurisprudencia, CNAEJurisprudencia, CNAE
from database import SessionLocal, Base, engine
ffrom app.api.database.session import datetime

# Cria as tabelas
Base.metadata.create_all(bind=engine)

def importar_jurisprudencias(path_csv: str):
    db: Session = SessionLocal()
    try:
        with open(path_csv, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            for row in reader:
                titulo = row['titulo'].strip()
                descricao = row['descricao'].strip()
                tribunal = row['tribunal'].strip()
                link = row['link_documento'].strip()
                uf = row['uf'].strip()
                data = datetime.strptime(row['data_publicacao'], "%Y-%m-%d").date()
                codigo_cnae = row['codigo_cnae'].strip()

                jurisprudencia = Jurisprudencia(
                    titulo=titulo,
                    descricao=descricao,
                    tribunal=tribunal,
                    link_documento=link,
                    uf=uf,
                    data_publicacao=data
                )
                db.add(jurisprudencia)
                db.flush()  # Garante ID disponível

                cnae = db.query(CNAE).filter_by(codigo_cnae=codigo_cnae).first()
                if cnae:
                    relacionamento = CNAEJurisprudencia(
                        cnae_id=cnae.id,
                        jurisprudencia_id=jurisprudencia.id
                    )
                    db.add(relacionamento)
            db.commit()
            print("✅ Jurisprudências importadas com sucesso.")
    except Exception as e:
        db.rollback()
        print(f"❌ Erro ao importar jurisprudências: {e}")
    finally:
        db.close()

# Exemplo de uso:
# importar_jurisprudencias("dados/jurisprudencias.csv")
