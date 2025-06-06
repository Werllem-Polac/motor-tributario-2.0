# Importando os módulos que criamos
from api.entrada_dados.leitor_csv import ler_arquivo_csv
from api.analise_tributaria.analisador_tributario import analisar_notas
from api.analise_operacional.analisador_operacional import analisar_operacao
from api.motor_estrategias.motor_estrategias import gerar_estrategias
from relatorios.gerador_relatorios import gerar_relatorio
from api.motor_estrategias.simulador_economico import simular_cenarios
from relatorios.gerador_excel import gerar_excel
from relatorios.gerador_pdf import gerar_pdf
from api.ia_motor.treinador_estrategias import treinamento_ia
from api.ia_motor.predictor_estrategias import prever_estrategias
from dashboard_motor import gerar_dashboard
from relatorios.gerador_relatorio_graficos import gerar_relatorio_graficos

# Caminho do arquivo CSV que contém as notas fiscais
caminho_arquivo = "entrada_dados/notas_exemplo.csv"

# Função principal do programa
def principal():
    print("🚀 Dados carregados com sucesso! Iniciando análises...")
    dados_notas = ler_arquivo_csv("api/entrada_dados/exemplo.csv")  # caminho real do seu CSV
    analisar_notas(dados_notas)
    gerar_excel(dados_notas)
    gerar_pdf(dados_notas)

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
    principal()
iif __name__ == "__main__":
    # Simulação de entrada
    dados_exemplo = [{"cnpj": "12345678000100"}, {"cnpj": "99887766000111"}]
    treinar_ia(dados_exemplo)