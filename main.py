# Importando os módulos que criamos
from api.entrada_dados.leitor_csv import ler_arquivo_csv
from analise_tributaria.analisador_tributario import analisar_notas
from analise_operacional.analisador_operacional import analisar_operacao
from motor_estrategias.motor_estrategias import gerar_estrategias
from relatorios.gerador_relatorios import gerar_relatorio
from motor_estrategias.simulador_economico import simular_cenarios
from relatorios.gerador_excel import gerar_excel
from relatorios.gerador_pdf import gerar_pdf
from ia_motor.treinador_estrategias import treinar_ia
from ia_motor.predictor_estrategias import prever_estrategias
from dashboard_motor import gerar_dashboard
from relatorios.gerador_relatorio_graficos import gerar_relatorio_graficos

# Caminho do arquivo CSV que contém as notas fiscais
caminho_arquivo = "entrada_dados/notas_exemplo.csv"

# Função principal do programa
def main():
    dados_notas = ler_arquivo_csv(caminho_arquivo)

    if dados_notas is not None:
        print("\n🚀 Dados carregados com sucesso! Iniciando análises...")

        analisar_notas(dados_notas)
        analisar_operacao(dados_notas)
        gerar_estrategias(dados_notas)

        gerar_relatorio(dados_notas)
        gerar_excel(dados_notas)
        gerar_pdf(dados_notas)

        simular_cenarios(dados_notas)

        treinar_ia(dados_notas)
        prever_estrategias(dados_notas)

        gerar_dashboard(dados_notas)
        gerar_relatorio_graficos()

        print("\n🏁 Todas as análises, relatórios, simulações, IA, previsões e dashboards concluídos com sucesso.")
    else:
        print("\n[ATENÇÃO] Não foi possível carregar os dados para análise.")

# Executar o programa
if __name__ == "__main__":
    main()