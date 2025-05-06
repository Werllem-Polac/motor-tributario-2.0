import re
import requests
import dash
from dash import dcc, html, Input, Output, State, callback_context
import dash_bootstrap_components as dbc

from upload_files.upload_area import layout_upload, registrar_callbacks_upload

API_URL = "http://127.0.0.1:8000"

# --- Inicialização do Dash ---
app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    suppress_callback_exceptions=True,
)
server = app.server

# --- Navbar (exibe após login) ---
navbar = dbc.Navbar(
    dbc.Container([
        dbc.NavbarBrand("Motor Tributário Inteligente", href="#"),
        dbc.Nav(
            dbc.DropdownMenu(
                nav=True, in_navbar=True, label="Perfil",
                children=[
                    dbc.DropdownMenuItem("Meus dados", id="perfil-meus-dados"),
                    dbc.DropdownMenuItem("Logout",     id="perfil-logout"),
                ],
            ),
            className="ms-auto", navbar=True
        ),
    ]),
    color="dark", dark=True, className="mb-4",
)

# --- Layout principal ---
app.layout = html.Div([
    dcc.Store(id="credentials", storage_type="local"),
    dcc.Store(id="auth-token",   storage_type="local"),
    dcc.Location(id="url"),

    html.Div(id="navbar", children=[navbar], style={"display": "none"}),

    dbc.Container([

        # Login
        html.Div(id="login-area", children=[
            dbc.Row([dbc.Col([
                html.H2("Login", className="text-center mb-4"),
                dbc.Input(id="login-email",    placeholder="Email",    type="email",    className="mb-2"),
                dbc.Input(id="login-password", placeholder="Senha",    type="password", className="mb-2"),
                dbc.Checklist(
                    options=[{"label":"Lembrar-me","value":"remember"}],
                    value=[], id="login-remember", switch=True, className="mb-2"
                ),
                dbc.Button("Entrar",            id="botao-login",      color="primary",   className="mb-2", style={"width":"100%"}),
                dbc.Button("Cadastrar Empresa", id="botao-cadastro",   color="secondary", className="mb-2", style={"width":"100%"}),
                html.Div(id="login-mensagem",   className="text-danger mt-2 text-center"),
                html.A("Esqueci minha senha", id="link-esqueci-senha",
                       style={"cursor":"pointer","fontSize":"0.9em","display":"block","marginTop":"8px"}),
            ], width=6, className="offset-md-3 mt-5")])
        ]),

        # Redefinir senha
        html.Div(id="reset-area", style={"display":"none"}, children=[
            html.H4("Redefinir senha", className="mb-3"),
            dbc.Input(id="reset-email", placeholder="Seu e-mail cadastrado", type="email", className="mb-2"),
            dbc.Button("Enviar link de reset", id="botao-reset", color="warning", style={"width":"100%"}),
            html.Div(id="reset-mensagem", className="mt-2 text-center"),
        ]),

        # Cadastro de Empresa
        html.Div(id="cadastro-area", style={"display":"none"}, children=[
            dbc.Row([dbc.Col([
                html.H2("Cadastro de Empresa", className="text-center mb-4"),

                # CNPJ com máscara automática
                dbc.Input(id="cadastro-cnpj", placeholder="00.000.000/0000-00", type="text",
                          maxLength=18, className="mb-2"),

                dbc.Input(id="cadastro-razao",      placeholder="Razão Social",  type="text",  className="mb-2"),
                dbc.Input(id="cadastro-logradouro", placeholder="Logradouro",     type="text",  className="mb-2"),
                dbc.Input(id="cadastro-numero",     placeholder="Número",         type="text",  className="mb-2"),
                dbc.Input(id="cadastro-bairro",     placeholder="Bairro",         type="text",  className="mb-2"),
                dbc.Input(id="cadastro-cidade",     placeholder="Cidade",         type="text",  className="mb-2"),
                dbc.Input(id="cadastro-estado",     placeholder="Estado (UF)",    type="text",  className="mb-2"),
                dbc.Input(id="cadastro-cep",        placeholder="00000-000",      type="text",  className="mb-2"),

                # Telefone com máscara automática
                dbc.Input(id="cadastro-telefone", placeholder="(27)99999-0000", type="text",
                          maxLength=14, className="mb-2"),

                dbc.Input(id="cadastro-email",      placeholder="Email",          type="email", className="mb-2"),

                # Senha e confirmação
                dbc.Input(id="cadastro-senha",         placeholder="Senha de Acesso",    type="password", className="mb-2"),
                dbc.Input(id="cadastro-senha-confirm", placeholder="Confirme a Senha",    type="password", className="mb-2"),

                # Critérios de senha
                html.Ul([
                    html.Li("Mínimo 8 caracteres",   id="crit-length",  style={"color":"red"}),
                    html.Li("1 letra minúscula",     id="crit-lower",   style={"color":"red"}),
                    html.Li("1 letra maiúscula",     id="crit-upper",   style={"color":"red"}),
                    html.Li("1 dígito",              id="crit-digit",   style={"color":"red"}),
                    html.Li("1 caractere especial",  id="crit-special", style={"color":"red"}),
                ], style={"listStyleType":"none","paddingLeft":0}),

                html.Div(id="senha-match-msg", className="mb-2"),

                dbc.Button("Salvar Empresa",        id="botao-salvar-cadastro",
                           color="success", className="mb-2", style={"width":"100%"}),
                dbc.Button("Voltar para Login",     id="botao-voltar-login",
                           color="secondary", className="mb-2", style={"width":"100%"}),
                html.Div(id="cadastro-mensagem",    className="mt-2 text-center"),

                dcc.ConfirmDialog(id="confirm-cadastro", message="CONFIRMAR DADOS"),
            ], width=6, className="offset-md-3 mt-5")])
        ]),

        # Dashboard
        html.Div(id="dashboard-area", style={"display":"none"}, children=[
            dbc.Row([dbc.Col(html.H2("Dashboard - Bem-vindo!", className="text-center mb-4"))]),
            dbc.Row([
                dbc.Col([
                    dbc.Button("Upload Arquivos",      id="botao-upload",     color="info",    className="mb-2", style={"width":"100%"}),
                    dbc.Button("Chat IA",              id="botao-chat-ia",    color="warning", className="mb-2", style={"width":"100%"}),
                    dbc.Button("Relatórios",           id="botao-relatorios", color="success", className="mb-2", style={"width":"100%"}),
                ], width=3),
                dbc.Col(html.Div(id="conteudo-dashboard"), width=9),
            ]),
        ]),

    ], fluid=True),
])

# --- Máscara de CNPJ ---
@app.callback(
    Output("cadastro-cnpj", "value"),
    Input("cadastro-cnpj", "value"),
)
def format_cnpj(value):
    if not value:
        return ""
    digits = re.sub(r"\D", "", value)[:14]
    mask = ""
    for i, c in enumerate(digits):
        mask += c
        if i == 1 or i == 4:
            mask += "."
        elif i == 7:
            mask += "/"
        elif i == 11:
            mask += "-"
    return mask

# --- Máscara de Telefone ---
@app.callback(
    Output("cadastro-telefone", "value"),
    Input("cadastro-telefone", "value"),
)
def format_phone(value):
    if not value:
        return ""
    digits = re.sub(r"\D", "", value)[:11]
    if len(digits) < 3:
        return f"({digits}"
    ddd, rest = digits[:2], digits[2:]
    if len(rest) <= 4:
        return f"({ddd}){rest}"
    return f"({ddd}){rest[:-4]}-{rest[-4:]}"

# --- Critérios de Senha ---
@app.callback(
    Output("crit-length","style"),
    Output("crit-lower","style"),
    Output("crit-upper","style"),
    Output("crit-digit","style"),
    Output("crit-special","style"),
    Input("cadastro-senha","value"),
)
def update_password_criteria(senha):
    ok, nok = {"color":"green"}, {"color":"red"}
    if not senha:
        return nok, nok, nok, nok, nok
    return (
        ok if len(senha)>=8 else nok,
        ok if re.search(r"[a-z]", senha) else nok,
        ok if re.search(r"[A-Z]", senha) else nok,
        ok if re.search(r"\d",    senha) else nok,
        ok if re.search(r"\W",    senha) else nok,
    )

# --- Confirmação de Senha ---
@app.callback(
    Output("senha-match-msg","children"),
    Input("cadastro-senha","value"),
    Input("cadastro-senha-confirm","value"),
)
def validate_password_match(senha, confirm):
    if not senha and not confirm:
        return ""
    if senha != confirm:
        return html.Span("❌ As senhas não coincidem.", style={"color":"red"})
    return html.Span("✅ Senhas iguais.",             style={"color":"green"})

# --- Mostrar Navbar após login ---
@app.callback(
    Output("navbar","style"),
    Input("auth-token","data"),
)
def toggle_nav(token):
    return {"display":"block"} if token else {"display":"none"}

# --- Navegação, login, cadastro, reset e logout UNIFICADOS ---
@app.callback(
    Output("login-area","style"),
    Output("reset-area","style"),
    Output("cadastro-area","style"),
    Output("dashboard-area","style"),
    Output("login-mensagem","children"),
    Output("reset-mensagem","children"),
    Output("auth-token","data"),
    Output("confirm-cadastro","displayed"),
    Output("cadastro-mensagem","children"),

    Input("botao-login","n_clicks"),
    Input("botao-cadastro","n_clicks"),
    Input("botao-voltar-login","n_clicks"),
    Input("link-esqueci-senha","n_clicks"),
    Input("botao-reset","n_clicks"),
    Input("perfil-logout","n_clicks"),
    Input("botao-salvar-cadastro","n_clicks"),
    Input("confirm-cadastro","submit_n_clicks"),
    Input("confirm-cadastro","cancel_n_clicks"),

    State("login-email","value"),
    State("login-password","value"),
    State("login-remember","value"),
    State("reset-email","value"),
    State("cadastro-cnpj","value"),
    State("cadastro-razao","value"),
    State("cadastro-logradouro","value"),
    State("cadastro-numero","value"),
    State("cadastro-bairro","value"),
    State("cadastro-cidade","value"),
    State("cadastro-estado","value"),
    State("cadastro-cep","value"),
    State("cadastro-telefone","value"),
    State("cadastro-email","value"),
    State("cadastro-senha","value"),
    State("cadastro-senha-confirm","value"),
    prevent_initial_call=True
)
def navigation_and_confirm(
    n_login,n_cad,n_voltar,n_forgot,n_reset,n_logout,
    n_salvar,n_submit,n_cancel,
    email,senha_login,remember,reset_email,
    cnpj,razao,logradouro,numero,bairro,
    cidade,estado,cep,telefone,email_cad,senha_cad,senha_conf
):
    ctx = callback_context.triggered[0]["prop_id"].split(".")[0]

    # Logout
    if ctx == "perfil-logout":
        return ({"display":"block"},{"display":"none"},{"display":"none"},{"display":"none"},
                "","",None, False, "")

    # Esqueci senha
    if ctx == "link-esqueci-senha":
        return ({"display":"none"},{"display":"block"},{"display":"none"},{"display":"none"},
                "","",None, False, "")
    if ctx == "botao-reset" and reset_email:
        try:
            requests.post(f"{API_URL}/password-reset-request",
                          data={"email":reset_email}, timeout=5)
            msg = "Se enviamos o link!"
        except:
            msg = "❌ Erro de conexão."
        return ({"display":"none"},{"display":"block"},{"display":"none"},{"display":"none"},
                "","",None, False, msg)

    # Mostrar cadastro
    if ctx == "botao-cadastro":
        return ({"display":"none"},{"display":"none"},{"display":"block"},{"display":"none"},
                "","",None, False, "")
    if ctx == "botao-voltar-login":
        return ({"display":"block"},{"display":"none"},{"display":"none"},{"display":"none"},
                "","",None, False, "")

    # Login
    if ctx == "botao-login":
        if not email or not senha_login:
            return dash.no_update, dash.no_update, dash.no_update, dash.no_update, \
                   "Informe email e senha","",None, False, ""
        try:
            r = requests.post(f"{API_URL}/login",
                              data={"username":email,"password":senha_login},
                              timeout=5)
            r.raise_for_status()
            token = r.json()["access_token"]
            return ({"display":"none"},{"display":"none"},{"display":"none"},{"display":"block"},
                    "","",token, False, "")
        except:
            return dash.no_update, dash.no_update, dash.no_update, dash.no_update, \
                   "❌ Login falhou","",None, False, ""

    # Abrir confirmação de cadastro
    if ctx == "botao-salvar-cadastro":
        return *([dash.no_update]*7), True, ""

    # Confirmar cadastro
    if ctx == "confirm-cadastro" and n_submit:
        if senha_cad != senha_conf:
            return *([dash.no_update]*7), False, "❌ Senhas não coincidem."
        payload = {
            "razao_social": razao,
            "cnpj":         cnpj,
            "logradouro":   logradouro,
            "numero":       numero,
            "bairro":       bairro,
            "cidade":       cidade,
            "estado":       estado,
            "cep":          cep,
            "telefone":     telefone,
            "email":        email_cad,
            "senha":        senha_cad
        }
        try:
            r = requests.post(f"{API_URL}/empresas/", json=payload, timeout=5)
            if r.status_code == 201:
                return ({"display":"block"},{"display":"none"},{"display":"none"},{"display":"none"},
                        "","",None, False, "✅ Cadastrado! Volte ao login.")
            detalhe = r.json().get("detail", r.status_code)
        except:
            detalhe = "Erro de conexão."
        return *([dash.no_update]*7), False, f"❌ {detalhe}"

    # Cancelar confirmação
    if ctx == "confirm-cadastro" and n_cancel:
        return *([dash.no_update]*7), False, ""

    return dash.no_update, dash.no_update, dash.no_update, dash.no_update, "", "", None, False, ""

# --- Conteúdo do Dashboard (único callback) ---
@app.callback(
    Output("conteudo-dashboard", "children"),
    Input("botao-upload",      "n_clicks"),
    Input("botao-chat-ia",     "n_clicks"),
    Input("botao-relatorios",  "n_clicks"),
    Input("perfil-meus-dados", "n_clicks"),
    State("auth-token",        "data"),
    prevent_initial_call=True
)
def render_conteudo(upload_click, chat_click, relatorios_click, perfil_click, token):
    ctx = callback_context.triggered[0]["prop_id"].split(".")[0]

    if ctx == "botao-upload":
        return layout_upload

    if ctx == "botao-chat-ia":
        return html.Div(html.H3("Chat IA em desenvolvimento 🚀", className="text-center"))

    if ctx == "botao-relatorios":
        return html.Div(html.H3("Relatórios em desenvolvimento 📊", className="text-center"))

    if ctx == "perfil-meus-dados":
        headers = {"Authorization":f"Bearer {token}"} if token else {}
        try:
            r = requests.get(f"{API_URL}/empresas/me", headers=headers, timeout=5)
            r.raise_for_status()
            u = r.json()
            return html.Div([
                html.H4("Meus Dados", className="mb-3"),
                html.P(f"Razão Social: {u['razao_social']}"),
                html.P(f"CNPJ: {u['cnpj']}"),
                html.P(f"Endereço: {u['logradouro']}, {u['numero']}"),
                html.P(f"Bairro: {u['bairro']}"),
                html.P(f"Cidade/UF: {u['cidade']}/{u['estado']}"),
                html.P(f"CEP: {u['cep']}"),
                html.P(f"Telefone: {u['telefone']}"),
                html.P(f"E-mail: {u['email']}"),
            ])
        except:
            return html.Div("❌ Erro de conexão com API.", className="text-danger")

    return dash.no_update

# --- Lembrar credenciais in client-side ---
@app.callback(
    Output("credentials","data"),
    Input("auth-token","data"),
    State("login-email","value"),
    State("login-remember","value"),
    prevent_initial_call=True
)
def save_cred(token,email,remember):
    if token and "remember" in remember:
        return {"email":email}
    return {}

@app.callback(
    Output("login-email","value"),
    Input("credentials","modified_timestamp"),
    State("credentials","data"),
    prevent_initial_call=True
)
def load_cred(ts,cred):
    if cred and "email" in cred:
        return cred["email"]
    raise dash.exceptions.PreventUpdate

# --- Registrar upload callbacks ---
registrar_callbacks_upload(app)

if __name__ == "__main__":
    app.run(debug=True)
