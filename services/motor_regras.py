from sqlalchemy.orm import Session
from models.models import CNAE, BeneficioFiscal, Jurisprudencia, CNAEBeneficio, CNAEJurisprudencia

class MotorRegrasTributarias:
    def __init__(self, db: Session, cnae: str, uf: str, regime: str):
        self.db = db
        self.cnae = cnae
        self.uf = uf
        self.regime = regime

    def analisar(self):
        resultados = {
            "beneficios_aplicaveis": [],
            "jurisprudencias_aplicaveis": [],
            "comentarios": []
        }

        cnae_obj = self.db.query(CNAE).filter_by(codigo_cnae=self.cnae).first()
        if not cnae_obj:
            resultados["comentarios"].append("CNAE não encontrado.")
            return resultados

        for rel in cnae_obj.beneficios:
            beneficio = rel.beneficio
            if self.uf in beneficio.abrangencia_uf:
                resultados["beneficios_aplicaveis"].append({
                    "nome": beneficio.nome,
                    "descricao": beneficio.descricao,
                    "tipo": beneficio.tipo
                })

        for rel in cnae_obj.jurisprudencias:
            jurisprudencia = rel.jurisprudencia
            if jurisprudencia.uf == self.uf:
                resultados["jurisprudencias_aplicaveis"].append({
                    "titulo": jurisprudencia.titulo,
                    "descricao": jurisprudencia.descricao,
                    "tribunal": jurisprudencia.tribunal
                })

        if not resultados["beneficios_aplicaveis"]:
            resultados["comentarios"].append("Nenhum benefício encontrado para este CNAE e UF.")

        if not resultados["jurisprudencias_aplicaveis"]:
            resultados["comentarios"].append("Nenhuma jurisprudência encontrada para este CNAE e UF.")

        return resultados
