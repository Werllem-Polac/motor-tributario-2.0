import dash
from dash import html, dcc, Input, Output, State, ctx
import dash_bootstrap_components as dbc
import requests

API_URL = "http://127.0.0.1:8000"

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)
server = app.server

app.layout = dbc.Container([
    dcc.Location(id="url"),
    dcc.Store(id="auth-token"),

    html.Div(id="login-layout", children=[
        html.H2("Login", className="text-center mt-4"),
        dbc.Input(id="login-email", placeholder="Email", type="email", className="mb-2"),
        dbc.Input(id="login-password", placeholder="Senha", type="password", className="mb-2"),
        dbc.Button("Entrar", id="btn-login", color="primary", className="mb-2 w-100"),
        html.Div(id="login-msg", className="text-danger text-center"),
        html.Hr(),
        dbc.Button("Cadastrar Nova Empresa", id="btn-cadastro", color="secondary", className="mb-2 w-100"),
    ]),

    html.Div(id="cadastro-layout", style={"display": "none"}, children=[
        html.H3("Cadastro de Empresa", className="text-center mt-4"),
        dbc.Input(id="cad-email", placeholder="Email", type="email", className="mb-2"),
        dbc.Input(id="cad-senha", placeholder="Senha", type="password", className="mb-2"),
        dbc.Input(id="cad-razao", placeholder="Razão Social", className="mb-2"),
        dbc.Input(id="cad-cnpj", placeholder="CNPJ", className="mb-2"),
        dbc.Button("Salvar Cadastro", id="btn-salvar-cadastro", color="success", className="mb-2 w-100"),
        dbc.Button("Voltar ao Login", id="btn-voltar-login", color="light", className="mb-2 w-100"),
        html.Div(id="cadastro-msg", className="text-success text-center")
    ]),

    html.Div(id="dashboard-layout", style={"display": "none"}, children=[
        html.H3("Dashboard Tributário por CNPJ", className="text-center mt-4"),
        dbc.Button("Logout", id="btn-logout", color="danger", className="mb-2"),
        html.Div("Bem-vindo ao sistema!"),
    ])
])

@app.callback(
    Output("login-layout", "style"),
    Output("cadastro-layout", "style"),
    Output("dashboard-layout", "style"),
    Output("login-msg", "children"),
    Output("cadastro-msg", "children"),
    Output("auth-token", "data"),
    Input("btn-login", "n_clicks"),
    Input("btn-cadastro", "n_clicks"),
    Input("btn-voltar-login", "n_clicks"),
    Input("btn-salvar-cadastro", "n_clicks"),
    Input("btn-logout", "n_clicks"),
    State("login-email", "value"),
    State("login-password", "value"),
    State("cad-email", "value"),
    State("cad-senha", "value"),
    State("cad-razao", "value"),
    State("cad-cnpj", "value"),
    prevent_initial_call=True
)
def navegar(login, cadastro, voltar, salvar, logout, login_email, login_senha, cad_email, cad_senha, razao, cnpj):
    acao = ctx.triggered_id

    if acao == "btn-cadastro":
        return {"display": "none"}, {"display": "block"}, {"display": "none"}, "", "", None

    if acao == "btn-voltar-login":
        return {"display": "block"}, {"display": "none"}, {"display": "none"}, "", "", None

    if acao == "btn-login":
        try:
            r = requests.post(f"{API_URL}/login", data={"username": login_email, "password": login_senha}, timeout=5)
            r.raise_for_status()
            token = r.json().get("access_token")
            return {"display": "none"}, {"display": "none"}, {"display": "block"}, "", "", token
        except:
            return dash.no_update, dash.no_update, dash.no_update, "Erro no login.", "", None
if acao == "btn-salvar-cadastro":
    try:
        payload = {"email": cad_email, "senha": cad_senha, "razao_social": razao, "cnpj": cnpj}
        r = requests.post(f"{API_URL}/empresas/", json=payload, timeout=5)
        r.raise_for_status()
        return {"display": "block"}, {"display": "none"}, {"display": "none"}, "", "Cadastro realizado com sucesso!", None
    except Exception as e:
        return dash.no_update, dash.no_update, dash.no_update, "", f"Erro ao salvar: {str(e)}", None


    if acao == "btn-logout":
        return {"display": "block"}, {"display": "none"}, {"display": "none"}, "", "", None

    return dash.no_update, dash.no_update, dash.no_update, "", "", None
    return dash.no_update, dash.no_update, dash.no_update, "", "Erro ao salvar", None


if __name__ == "__main__":
    app.run(debug=True)
