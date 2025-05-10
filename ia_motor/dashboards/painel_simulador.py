import dash
from dash import html, dcc, Input, Output, State
import dash_bootstrap_components as dbc

teses = ["crédito presumido", "desoneração de insumos", "tese da essencialidade"]

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

app.layout = dbc.Container([
    html.H2("🧮 Simulador Fiscal por Tese"),
    dbc.Input(id="input_cnpj", placeholder="Digite o CNPJ", type="text"),
    dcc.Dropdown(id="dropdown_tese", options=[{"label": t, "value": t} for t in teses], placeholder="Selecione a tese"),
    html.Br(),
    dbc.Button("Simular", id="btn-simular", color="warning"),
    html.Br(), html.Br(),
    html.Div(id="resultado_simulador")
])

@app.callback(
    Output("resultado_simulador", "children"),
    Input("btn-simular", "n_clicks"),
    State("input_cnpj", "value"),
    State("dropdown_tese", "value")
)
def simular(n, cnpj, tese):
    if not cnpj or not tese:
        return "⚠️ Por favor, informe o CNPJ e selecione a tese."
    economia = round(500000 * 0.05, 2)
    return f"📈 Economia estimada para {cnpj} com '{tese}': R$ {economia}"

if __name__ == "__main__":
    app.run(debug=True)

