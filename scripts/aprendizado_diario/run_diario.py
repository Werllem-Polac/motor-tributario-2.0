from . import (
    crawler_stf, crawler_sefaz,
    extrator_texto, gerar_embeddings, integrador_motor
)

def executar_pipeline():
    print("Iniciando aprendizado jurídico diário...")

    # 1. Coleta de dados
    print("Coletando jurisprudências do STF...")
    stf_docs = crawler_stf.coletar()

    print("Coletando atos da SEFAZ por UF...")
    sefaz_docs = crawler_sefaz.coletar()

    # 2. Limpeza e estruturação
    print("Processando textos...")
    textos = extrator_texto.processar(stf_docs + sefaz_docs)

    # 3. Geração de embeddings
    print("Gerando embeddings...")
    vetores = gerar_embeddings.gerar(textos)

    # 4. Armazenamento
    print("Salvando no motor de conhecimento...")
    integrador_motor.salvar(vetores)

    print("✅ Aprendizado diário concluído!")

if __name__ == "__main__":
    executar_pipeline()
