import pandas as pd
import matplotlib.pyplot as plt
import os

def gerar_dashboard(dados):
    print("\n📊 Iniciando geração do Dashboard Gráfico...")

    # ✅ Garantir que os dados sejam um DataFrame
    if isinstance(dados, list):
        dados = pd.DataFrame(dados)
    elif isinstance(dados, dict):
        dados = pd.DataFrame([dados])
    elif not isinstance(dados, pd.DataFrame):
        print("[ERRO] Formato de dados não suportado.")
        return

    if dados.empty:
        print("[ERRO] Nenhum dado válido encontrado para gerar o Dashboard.")
        return

    # 🔍 Detectar automaticamente a coluna de valor
    coluna_valor = next((col for col in dados.columns if 'valor' in col.lower()), None)
    if not coluna_valor:
        print("[ERRO] Nenhuma coluna de valor encontrada no CSV.")
        return

    # Criar a pasta de gráficos se não existir
    pasta_graficos = "graficos"
    os.makedirs(pasta_graficos, exist_ok=True)

    # 1️⃣ Estratégias aplicadas por tipo de produto
    estrategias_produto = []
    for _, nota in dados.iterrows():
        produto = str(nota.get('Produto', ''))
        ncm = str(nota.get('NCM', ''))

        if ncm.startswith('02'):
            estrategias_produto.append(("Tese da Desossa + Essencialidade", produto))
        elif ncm.startswith('05') or 'Ossos' in produto or 'Sebos' in produto:
            estrategias_produto.append(("Imunidade Agropecuária (Subprodutos)", produto))
        elif ncm.startswith('23'):
            estrategias_produto.append(("Regime Especial para Ração Animal", produto))
        else:
            estrategias_produto.append(("Análise Manual", produto))

    df_estrategias_produto = pd.DataFrame(estrategias_produto, columns=["Estratégia", "Produto"])

    plt.figure(figsize=(10,6))
    df_estrategias_produto["Estratégia"].value_counts().plot(kind='bar')
    plt.title('Estratégias Aplicadas por Tipo de Produto')
    plt.xlabel('Estratégia')
    plt.ylabel('Quantidade de Produtos')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(pasta_graficos, "estrategias_por_produto.png"))
    plt.close()

    # 2️⃣ Economia simulada por estratégia
    economia_estrategias = []
    for _, nota in dados.iterrows():
        valor = float(nota.get(coluna_valor, 0))
        produto = str(nota.get('Produto', ''))
        ncm = str(nota.get('NCM', ''))

        if ncm.startswith('02'):
            economia = valor * 0.08
            economia_estrategias.append(("Tese da Desossa + Essencialidade", economia))
        elif ncm.startswith('05') or 'Ossos' in produto or 'Sebos' in produto:
            economia = valor * 0.12
            economia_estrategias.append(("Imunidade Agropecuária (Subprodutos)", economia))
        elif ncm.startswith('23'):
            economia = valor * 0.0925
            economia_estrategias.append(("Regime Especial para Ração Animal", economia))
        else:
            economia_estrategias.append(("Análise Manual", 0))

    df_economia = pd.DataFrame(economia_estrategias, columns=["Estratégia", "Economia"])
    economia_agrupada = df_economia.groupby("Estratégia").sum()

    plt.figure(figsize=(10,6))
    economia_agrupada["Economia"].plot(kind='bar')
    plt.title('Economia Simulada por Tipo de Estratégia')
    plt.xlabel('Estratégia')
    plt.ylabel('Economia Estimada (R$)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(pasta_graficos, "economia_por_estrategia.png"))
    plt.close()

    # 3️⃣ Comparativo de tributos: antes vs depois
    total_valor_produtos = dados[coluna_valor].astype(float).sum()
    icms_atual = total_valor_produtos * 0.12
    pis_cofins_atual = total_valor_produtos * 0.0925
    total_tributos_atual = icms_atual + pis_cofins_atual

    icms_simulado = icms_atual * 0.6
    pis_cofins_simulado = pis_cofins_atual * 0.5
    total_tributos_simulado = icms_simulado + pis_cofins_simulado

    comparativo = pd.DataFrame({
        "Cenário Atual": [total_tributos_atual],
        "Cenário Otimizado": [total_tributos_simulado]
    })

    plt.figure(figsize=(8,5))
    comparativo.T.plot(kind='bar', legend=False)
    plt.title('Comparativo de Tributos: Atual vs Otimizado')
    plt.ylabel('Tributos (R$)')
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig(os.path.join(pasta_graficos, "comparativo_tributos.png"))
    plt.close()

    # 4️⃣ Top 10 produtos que mais economizam
    top10_economia = df_economia.copy()
    top10_economia['Produto'] = dados['Produto'].values[:len(top10_economia)]
    top10_top = top10_economia.groupby('Produto')['Economia'].sum().sort_values(ascending=False).head(10)

    plt.figure(figsize=(12,6))
    top10_top.plot(kind='barh')
    plt.title('Top 10 Produtos que mais Geram Economia')
    plt.xlabel('Economia Estimada (R$)')
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.savefig(os.path.join(pasta_graficos, "top10_produtos_economia.png"))
    plt.close()

    # 5️⃣ Pie: estratégias que mais impactam na economia
    plt.figure(figsize=(10,6))
    economia_agrupada["Economia"].sort_values(ascending=False).plot(kind='pie', autopct='%1.1f%%', startangle=90)
    plt.title('Estratégias que Mais Impactam na Economia')
    plt.ylabel('')
    plt.tight_layout()
    plt.savefig(os.path.join(pasta_graficos, "impacto_estrategias.png"))
    plt.close()

    # 6️⃣ Produtos sem estratégia clara
    produtos_alerta = df_estrategias_produto[df_estrategias_produto['Estratégia'] == 'Análise Manual']
    plt.figure(figsize=(8,5))
    plt.bar(['Produtos sem Estratégia'], [produtos_alerta.shape[0]])
    plt.title('Produtos Sem Estratégia Clara (Alerta)')
    plt.ylabel('Quantidade de Produtos')
    plt.tight_layout()
    plt.savefig(os.path.join(pasta_graficos, "produtos_sem_estrategia.png"))
    plt.close()

    # 7️⃣ CFOP Interno vs Interestadual
    cfop_series = dados['CFOP'].astype(str).apply(lambda x: 'Interno' if x.startswith('5') else ('Interestadual' if x.startswith('6') else 'Outro'))
    plt.figure(figsize=(8,5))
    cfop_series.value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=90)
    plt.title('Distribuição de Operações: Internas vs Interestaduais')
    plt.ylabel('')
    plt.tight_layout()
    plt.savefig(os.path.join(pasta_graficos, "cfop_interno_interestadual.png"))
    plt.close()

    print("✅ Gráficos gerados com sucesso na pasta 'graficos/'")
