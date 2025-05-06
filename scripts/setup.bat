@echo off
REM scripts/setup.bat - Inicializador completo do Motor Tributário no Windows

cd /d %~dp0..

ECHO ===== Iniciando API (FastAPI) =====
start cmd /k "cd api && call venv\Scripts\activate && uvicorn main:app --reload"

TIMEOUT /T 3

ECHO ===== Iniciando Dashboard (Dash) =====
start cmd /k "cd dashboard && call venv\Scripts\activate && python app.py"

ECHO.
ECHO ✅ Motor Tributário inicializado com sucesso.
ECHO Acesse http://127.0.0.1:8000/docs para testar a API
ECHO Acesse http://127.0.0.1:8050 para ver o Dashboard
