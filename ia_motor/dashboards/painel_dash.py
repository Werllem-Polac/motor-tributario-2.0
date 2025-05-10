import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server  # para deploy

app.layout = dbc.Container([
    html.H1("📊 Painel Tributário - Visão Geral"),
    html.Hr(),
    dbc.Row([
        dbc.Col([
            html.H4("Empresas Cadastradas"),
            html.Ul(id="lista_empresas", children=[
                html.Li("CNPJ 11.111.111/0001-11 - Empresa Exemplo"),
                html.Li("CNPJ 22.222.222/0001-22 - Outra Empresa")
            ])
        ]),
        dbc.Col([
            html.H4("Análises Recentes"),
            html.Ul([
                html.Li("Empresa Exemplo: Economia R$ 42.300 via crédito presumido"),
                html.Li("Outra Empresa: Risco 85% na ST - Tese da essencialidade aplicada")
            ])
        ])
    ])
])

if __name__ == "__main__":
    app.run(debug=True)

