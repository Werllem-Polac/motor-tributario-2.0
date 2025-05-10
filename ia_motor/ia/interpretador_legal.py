def interpretar_contexto(cnpj: str, pergunta: str) -> str:
    if "crédito" in pergunta.lower():
        return (
            f"Com base no histórico do CNPJ {cnpj}, é possível aplicar a tese do crédito presumido "
            f"nos termos do art. 3º da Lei nº 10.833/2003, combinado com jurisprudência do STJ."
        )
    elif "essencialidade" in pergunta.lower():
        return (
            f"O princípio da essencialidade pode ser defendido para o CNPJ {cnpj} com base no art. 155, §2º, II, da CF/88, "
            f"considerando a relevância do insumo na cadeia de produção."
        )
    else:
        return (
            f"Para o CNPJ {cnpj}, a resposta jurídica dependerá de análise detalhada do regime tributário, NCM e UF. "
            f"Recomenda-se gerar parecer técnico com base completa de jurisprudência."
        )
