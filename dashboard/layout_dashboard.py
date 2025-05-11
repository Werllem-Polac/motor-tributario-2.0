import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
import plotly.express as px
import pandas as pd

# Dados simulados para visualização (substituir por dados reais)
df = pd.DataFrame({
    "CNAE": ["1011-2/01", "1031-7/00", "4711-3/01"],
    "Benefícios Aplicados": [4, 2, 1],
    "Jurisprudências Relevantes": [3, 1, 2],
    "Tipo": ["Indústria", "Indústria", "Comércio"]
})

def layout_dashboard():
    grafico_beneficios = px.bar(df, x="CNAE", y="Benefícios Aplicados", color="Tipo", barmode="group")
    grafico_juris = px.bar(df, x="CNAE", y="Jurisprudências Relevantes", color="Tipo", barmode="group")

    return dbc.Container([
        html.H2("📊 Visão Geral Tributária", className="text-center my-4"),

        dbc.Row([
            dbc.Col(dcc.Graph(figure=grafico_beneficios), md=6),
            dbc.Col(dcc.Graph(figure=grafico_juris), md=6),
        ]),

        html.Div("🔍 Este painel exibe uma visão sintética dos dados tributários por CNAE."),
    ], fluid=True)
