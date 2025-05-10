# scripts/executar_fluxo_lote.py

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from api.entrada_dados.leitor_csv import ler_arquivo_csv
from api.analise_tributaria.analisador_tributario import analisar_notas
from api.analise_operacional.analisador_operacional import analisar_operacao
from api.motor_estrategias.motor_estrategias import gerar_estrategias
from api.motor_estrategias.simulador_economico import simular_cenarios
from api.ia_motor.treinador_estrategias import treinar_ia
from ia_motor.ia.predictor_estrategias import prever_estrategias
from relatorios.gerador_relatorios import gerar_relatorio
from relatorios.gerador_excel import gerar_excel
from relatorios.gerador_pdf import gerar_pdf
from relatorios.gerador_relatorio_graficos import gerar_relatorio_graficos
from dashboard_motor import gerar_dashboard

# Caminho do arquivo CSV de entrada
CAMINHO_ARQUIVO = "api/entrada_dados/exemplo.csv"

def fluxo_completo():
    print("🚀 Iniciando execução em lote com base no arquivo:", CAMINHO_ARQUIVO)
    
    dados_notas = ler_arquivo_csv(CAMINHO_ARQUIVO)

    if dados_notas is None or dados_notas.empty:
        print("❌ Arquivo vazio ou inválido.")
        return

    print("✅ Dados carregados. Iniciando pipeline:")

    analisar_notas(dados_notas)
    analisar_operacao(dados_notas)
    gerar_estrategias(dados_notas)
    simular_cenarios(dados_notas)

    gerar_relatorio(dados_notas)
    gerar_excel(dados_notas)
    gerar_pdf(dados_notas)
    gerar_dashboard(dados_notas)
    gerar_relatorio_graficos()

    treinar_ia(dados_notas)
    prever_estrategias(dados_notas)

    print("🏁 Execução concluída com sucesso.")

if __name__ == "__main__":
    fluxo_completo()
