# 🧠 Executar este script no terminal Python para importar CNAEs
# Certifique-se que os arquivos estão no lugar certo e as dependências instaladas

import os
from dotenv import load_dotenv
from sqlalchemy.orm import Session
from models.models import CNAE
from database import SessionLocal, Base, engine
import csv

# 🔁 Carrega variáveis do arquivo .env
load_dotenv()

# 🛠 Garante que as tabelas existem
Base.metadata.create_all(bind=engine)

# 📥 Função para importar CNAEs a partir de um CSV
def importar_cnaes(path_csv: str):
    db: Session = SessionLocal()
    try:
        with open(path_csv, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            for row in reader:
                codigo = row['Código'].strip()
                descricao = row['Título'].strip()
                tipo = "Indústria" if codigo.startswith("1") else "Comércio"  # lógica simples
                cnae = CNAE(codigo_cnae=codigo, descricao=descricao, tipo_atividade=tipo)
                db.add(cnae)
            db.commit()
            print("✅ CNAEs importados com sucesso.")
    except Exception as e:
        print(f"❌ Erro ao importar CNAEs: {e}")
        db.rollback()
    finally:
        db.close()

# 📍 Caminho relativo do arquivo CSV
caminho_csv = "dados/cnae-subclasses.csv"

# ▶️ Executa a função
importar_cnaes(caminho_csv)
