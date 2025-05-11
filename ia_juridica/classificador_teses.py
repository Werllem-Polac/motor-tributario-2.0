import json
from ia_juridica.embeddings_manager import gerar_embedding, similaridade

def classificar_tese(texto_empresa: str, limite_analogia=0.85):
    emb_empresa = gerar_embedding(texto_empresa)
    with open("ia_juridica/base_teses.json", "r", encoding="utf-8") as f:
        teses = json.load(f)

    melhores = []
    for tese in teses:
        emb_tese = gerar_embedding(tese["descricao"])
        sim = similaridade(emb_empresa, emb_tese)
        melhores.append({
            "tese_id": tese["id"],
            "tese_nome": tese["nome"],
            "descricao": tese["descricao"],
            "similaridade": sim
        })

    melhores.sort(key=lambda x: x["similaridade"], reverse=True)
    top = melhores[0]
    
    if top["similaridade"] < limite_analogia:
        from ia_juridica.analogia_tributaria import aplicar_analogia
        return aplicar_analogia(texto_empresa, emb_empresa, melhores)

    top["origem"] = {
        "tipo": "correspondencia_direta",
        "similaridade": top["similaridade"],
        "justificativa": "Tese aplicada com correspondência direta, sem uso de analogia."
    }
    return top
