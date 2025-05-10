def gerar_prompt(tese: str, contexto: str = "") -> str:
    return (
        f"Considere apenas jurisprudência consolidada e legislação vigente. "
        f"Avalie a tese '{tese}' com base nos fundamentos legais e administrativos. "
        f"Contexto adicional: {contexto}"
    )
