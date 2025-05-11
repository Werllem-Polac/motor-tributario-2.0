from ia_juridica.embeddings_manager import similaridade

def aplicar_analogia(texto_empresa, emb_empresa, candidatos):
    base = candidatos[0]
    return {
        "tese_id": base["tese_id"],
        "tese_nome": base["tese_nome"],
        "descricao": base["descricao"],
        "similaridade": base["similaridade"],
        "origem": {
            "tipo": "analogia",
            "base_tese_similar": base["tese_nome"],
            "similaridade": base["similaridade"],
            "justificativa": (
                "Nenhuma tese se encaixou diretamente com alta similaridade. "
                "Aplicada analogia com a tese mais próxima baseada na atividade e descrição informada. "
                "Fundamentação jurídica no art. 108, §1º do CTN."
            )
        }
    }
