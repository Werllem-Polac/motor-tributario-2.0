import csv
from sqlalchemy.orm import Session
from models.models import BeneficioFiscal, CNAEBeneficio, CNAE
from app.api.database.session import SessionLocal, Base, engine

# Garante criação das tabelas
Base.metadata.create_all(bind=engine)

def importar_beneficios(path_csv: str):
    db: Session = SessionLocal()
    try:
        with open(path_csv, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            for row in reader:
                nome = row['nome'].strip()
                tipo = row['tipo'].strip()
                descricao = row['descricao'].strip()
                abrangencia = [uf.strip() for uf in row['abrangencia_uf'].split(',')]
                codigo_cnae = row['codigo_cnae'].strip()

                beneficio = BeneficioFiscal(
                    nome=nome,
                    tipo=tipo,
                    descricao=descricao,
                    abrangencia_uf=abrangencia,
                    ativo=True
                )
                db.add(beneficio)
                db.flush()  # Garante que o ID está disponível

                cnae = db.query(CNAE).filter_by(codigo_cnae=codigo_cnae).first()
                if cnae:
                    relacionamento = CNAEBeneficio(cnae_id=cnae.id, beneficio_id=beneficio.id)
                    db.add(relacionamento)
            db.commit()
            print("✅ Benefícios importados com sucesso.")
    except Exception as e:
        db.rollback()
        print(f"❌ Erro ao importar benefícios: {e}")
    finally:
        db.close()

# Exemplo de uso:
# importar_beneficios("dados/beneficios.csv")

