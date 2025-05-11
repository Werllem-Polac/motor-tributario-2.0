from typing import List, Dict

class AuditorFiscalInteligente:
    def __init__(self, documentos: List[Dict]):
        self.documentos = documentos

    def validar_cfop(self, doc):
        cfop = doc.get("cfop", "")
        if not cfop or len(cfop) != 4:
            return "CFOP inválido"
        return None

    def validar_cst(self, doc):
        cst = doc.get("cst", "")
        if not cst or not cst.isdigit():
            return "CST inválido"
        return None

    def auditar(self):
        erros = []
        for doc in self.documentos:
            doc_erros = {
                "chave": doc.get("chave", "sem-chave"),
                "erros": []
            }
            cfop_erro = self.validar_cfop(doc)
            cst_erro = self.validar_cst(doc)
            if cfop_erro:
                doc_erros["erros"].append(cfop_erro)
            if cst_erro:
                doc_erros["erros"].append(cst_erro)
            if doc_erros["erros"]:
                erros.append(doc_erros)
        return erros
