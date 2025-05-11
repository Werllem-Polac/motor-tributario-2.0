from ia_juridica.classificador_teses import classificar_tese
from ia_juridica.extrator_basico import extrair_entidades
from ia_juridica.perguntas_respostas import responder_pergunta
import ia_juridica.resultados as log

def analisar_texto_empresa(texto: str):
    """
    Processa o texto de descrição da empresa e retorna a tese mais aplicável,
    podendo usar analogia se necessário.
    """
    entidades = extrair_entidades(texto)
    resultado = classificar_tese(texto)

    log.registrar_resultado({
        "entrada": texto,
        "entidades": entidades,
        "tese": resultado
    })

    return {
        "entidades_extraidas": entidades,
        "tese_recomendada": resultado
    }
