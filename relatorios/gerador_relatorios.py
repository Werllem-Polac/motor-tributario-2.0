import os

def gerar_relatorio(dados):
    if dados is None:
        print("[ERRO] Nenhum dado foi carregado para o Gerador de Relatórios.")
        return

    # Criar a pasta de saída se não existir
    pasta_saida = "relatorios"
    if not os.path.exists(pasta_saida):
        os.makedirs(pasta_saida)

    # Nome do arquivo de relatório
    caminho_relatorio = os.path.join(pasta_saida, "relatorio_estrategias.txt")

    try:
        with open(caminho_relatorio, "w", encoding="utf-8") as arquivo:
            arquivo.write("Relatório de Estratégias Tributárias e Operacionais\n")
            arquivo.write("===============================================\n\n")

            for index, nota in dados.iterrows():
                produto = nota['Produto']
                ncm = str(nota['NCM'])
                cfop = str(nota['CFOP'])
                cst = str(nota['CST'])

                estrategias = []

                if ncm.startswith('02'):
                    estrategias.append(("Aplicar Tese da Desossa + Essencialidade", 10))

                if ncm.startswith('05') or 'Ossos' in produto or 'Sebos' in produto:
                    estrategias.append(("Aplicar Tese da Imunidade Agropecuária (Subprodutos)", 8))

                if ncm.startswith('23'):
                    estrategias.append(("Aplicar Regime Especial para Ração Animal (Isenção de PIS/COFINS)", 7))

                if cfop == '5102':
                    estrategias.append(("Aproveitamento de crédito presumido de ICMS (Operação Interna)", 6))

                if cst.startswith('0') or cst.startswith('1'):
                    estrategias.append(("Analisar possibilidade de crédito integral de ICMS", 5))

                if estrategias:
                    arquivo.write(f"Produto: {produto}\n")
                    estrategias_ordenadas = sorted(estrategias, key=lambda x: x[1], reverse=True)
                    for estrategia, prioridade in estrategias_ordenadas:
                        arquivo.write(f" - Estratégia: {estrategia} (Prioridade: {prioridade})\n")
                    arquivo.write("\n")
                else:
                    arquivo.write(f"Produto: {produto}\n")
                    arquivo.write(" - Nenhuma estratégia tributária clara detectada.\n\n")

            print(f"\n Relatório gerado com sucesso em: {caminho_relatorio}")

    except Exception as e:
        print(f"[ERRO] Falha ao gerar o relatório: {e}")