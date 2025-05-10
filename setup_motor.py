import os

estrutura = {
    "ia_motor": [
        "main.py",
        "config.py",
        "README.md"
    ],
    "ia_motor/database": [
        "engine.py",
        "models.py",
        "utils.py",
        "__init__.py"
    ],
    "ia_motor/rotas": [
        "empresas.py",
        "analise_xml.py",
        "pareceres.py",
        "simulador.py",
        "lote_analise.py",
        "chat_tributario.py",
        "__init__.py"
    ],
    "ia_motor/services": [
        "processador_xml.py",
        "classificador_risco.py",
        "auto_estrategista.py",
        "gerador_defesa.py",
        "simulador_fiscal.py",
        "atualizador_ia.py",
        "__init__.py"
    ],
    "ia_motor/ia": [
        "embeddings_juridicos.py",
        "prompt_engineering.py",
        "gerador_teses_ocultas.py",
        "crawler_jurisprudencia.py",
        "interpretador_legal.py",
        "memoria_global.py",
        "__init__.py"
    ],
    "ia_motor/chatbot": [
        "chat_router.py",
        "chat_core.py",
        "chat_logger.py",
        "resposta_formatada.py",
        "__init__.py"
    ],
    "ia_motor/dashboards": [
        "painel_dash.py",
        "painel_lote.py",
        "painel_chat.py",
        "painel_simulador.py",
        "__init__.py"
    ],
    "ia_motor/tests": [
        "test_risco.py",
        "test_parecer.py",
        "test_simulador.py",
        "test_chat.py",
        "__init__.py"
    ]
}

def criar_estrutura():
    for pasta, arquivos in estrutura.items():
        os.makedirs(pasta, exist_ok=True)
        for arquivo in arquivos:
            caminho_arquivo = os.path.join(pasta, arquivo)
            if not os.path.exists(caminho_arquivo):
                with open(caminho_arquivo, "w", encoding="utf-8") as f:
                    if arquivo.endswith(".py"):
                        f.write(f'"""Arquivo: {arquivo}\nMódulo: {pasta}\nDescrição: IMPLEMENTAR\n"""\n\n')
    print("✅ Estrutura do Motor Tributário 2.0 criada com sucesso!")

if __name__ == "__main__":
    criar_estrutura()
