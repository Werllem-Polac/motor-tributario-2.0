import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px
import os
from datetime import datetime
from gerador_pdf import gerar_relatorio_pdf
from gerador_excel import gerar_relatorio_excel

# Inicializar o app
app = dash.Dash(__name__, external_stylesheets=["/assets/style.css"])
server = app.server

# Empresas disponíveis
empresas = {
    "Empresa A": "dados_empresaA.csv",
    "Empresa B": "dados_empresaB.csv"
}

# Tipos de gráfico disponíveis
tipos_graficos = {
    "Barra: Valor Econômico": "bar",
    "Pizza: Estratégias Aplicadas": "pie",
    "Linha: Evolução da Economia Fiscal (%)": "line"
}

# Função para carregar dados baseado na empresa
def carregar_dados_empresa(empresa):
    caminho = os.path.join("base_dados", empresas[empresa])
    return pd.read_csv(caminho)

# Layout
app.layout = html.Div([
    html.Header([
        html.H1("Motor Tributário Inteligente", className="header-title"),
        html.P(f"Data: {datetime.today().strftime('%d/%m/%Y')}", className="header-date")
    ], className="header"),

    html.Section([
        html.Label("Selecionar Empresa:", className="dropdown-label"),
        dcc.Dropdown(
            id='empresa-dropdown',
            options=[{'label': nome, 'value': nome} for nome in empresas.keys()],
            value=list(empresas.keys())[0],
            className="dropdown-style"
        )
    ]),

    html.Br(),

    html.Section([
        html.Div(id="kpi-container", className="kpi-container")
    ]),

    html.Br(),

    html.Section([
        html.Label("Filtrar Produto:", className="dropdown-label"),
        dcc.Dropdown(id='filtro-produto', multi=True, placeholder="Selecione Produto(s)...", className="dropdown-style"),

        html.Label("Filtrar NCM:", className="dropdown-label"),
        dcc.Dropdown(id='filtro-ncm', multi=True, placeholder="Selecione NCM(s)...", className="dropdown-style"),

        html.Label("Filtrar CFOP:", className="dropdown-label"),
        dcc.Dropdown(id='filtro-cfop', multi=True, placeholder="Selecione CFOP(s)...", className="dropdown-style"),

        html.Label("Filtrar Estratégia Aplicada:", className="dropdown-label"),
        dcc.Dropdown(id='filtro-estrategia', multi=True, placeholder="Selecione Estratégia(s)...", className="dropdown-style"),

        html.Label("Selecionar Tipo de Gráfico:", className="dropdown-label"),
        dcc.Dropdown(
            id='filtro-tipo-grafico',
            options=[{'label': k, 'value': v} for k, v in tipos_graficos.items()],
            value="bar",
            className="dropdown-style"
        ),
    ]),

    html.Br(),

    html.Div([
        html.Button("📄 Exportar PDF", id="exportar-pdf", n_clicks=0, className="export-button"),
        html.Button("📄 Exportar Excel", id="exportar-excel", n_clicks=0, className="export-button")
    ], style={'textAlign': 'center'}),

    html.Br(),

    html.Div(id='grafico-display', className="grafico-container"),

    dcc.Download(id="download-pdf"),
    dcc.Download(id="download-excel"),
])

# Atualizar Filtros e KPIs
@app.callback(
    Output('filtro-produto', 'options'),
    Output('filtro-ncm', 'options'),
    Output('filtro-cfop', 'options'),
    Output('filtro-estrategia', 'options'),
    Output('kpi-container', 'children'),
    Input('empresa-dropdown', 'value')
)
def atualizar_filtros_e_kpis(empresa_selecionada):
    df = carregar_dados_empresa(empresa_selecionada)

    produtos = [{'label': p, 'value': p} for p in df["Produto"].unique()]
    ncm_options = [{'label': f"{row['NCM']} - {row['Produto']}", 'value': row['NCM']} for idx, row in df.iterrows()]
    cfops = [{'label': c, 'value': c} for c in df["CFOP"].unique()]
    estrategias = [{'label': e, 'value': e} for e in df["Estrategia"].unique()]

    kpis = html.Div([
        html.Div([
            html.H4("Produtos Analisados"),
            html.H2(f"{len(df)}")
        ], className="kpi-card"),

        html.Div([
            html.H4("Economia Fiscal Estimada"),
            html.H2(f"R$ {df['Valor_Produto'].sum() * df['Economia_Percentual'].mean() / 100:,.2f}")
        ], className="kpi-card"),

        html.Div([
            html.H4("Estratégias Aplicadas"),
            html.H2(f"{df['Estrategia'].nunique()}")
        ], className="kpi-card")
    ])

    return produtos, ncm_options, cfops, estrategias, kpis

# Atualizar Gráfico
@app.callback(
    Output('grafico-display', 'children'),
    Input('empresa-dropdown', 'value'),
    Input('filtro-produto', 'value'),
    Input('filtro-ncm', 'value'),
    Input('filtro-cfop', 'value'),
    Input('filtro-estrategia', 'value'),
    Input('filtro-tipo-grafico', 'value')
)
def atualizar_grafico(empresa, produtos, ncms, cfops, estrategias, tipo_grafico):
    df = carregar_dados_empresa(empresa)

    if produtos:
        df = df[df["Produto"].isin(produtos)]
    if ncms:
        df = df[df["NCM"].isin(ncms)]
    if cfops:
        df = df[df["CFOP"].isin(cfops)]
    if estrategias:
        df = df[df["Estrategia"].isin(estrategias)]

    if not df.empty:
        if tipo_grafico == "bar":
            fig = px.bar(df, x="Produto", y="Valor_Produto", color="Estrategia", title="Valor Econômico dos Produtos")
        elif tipo_grafico == "pie":
            fig = px.pie(df, names="Estrategia", title="Distribuição das Estratégias Aplicadas")
        elif tipo_grafico == "line":
            fig = px.line(df, x="Produto", y="Economia_Percentual", title="Evolução da Economia Fiscal (%)")
        return dcc.Graph(figure=fig)
    else:
        fig_vazio = px.scatter(title="Nenhum dado disponível para exibir.")
        return dcc.Graph(figure=fig_vazio)

# Exportar PDF
@app.callback(
    Output("download-pdf", "data"),
    Input("exportar-pdf", "n_clicks"),
    Input('empresa-dropdown', 'value'),
    prevent_initial_call=True
)
def exportar_pdf(n_clicks, empresa):
    df = carregar_dados_empresa(empresa)
    nome_arquivo = gerar_relatorio_pdf(df, empresa)
    return dcc.send_file(nome_arquivo)

# Exportar Excel
@app.callback(
    Output("download-excel", "data"),
    Input("exportar-excel", "n_clicks"),
    Input('empresa-dropdown', 'value'),
    prevent_initial_call=True
)
def exportar_excel(n_clicks, empresa):
    df = carregar_dados_empresa(empresa)
    nome_arquivo = gerar_relatorio_excel(df, empresa)
    return dcc.send_file(nome_arquivo)

# Rodar servidor
if __name__ == "__main__":
    app.run(debug=True)
