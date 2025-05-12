FROM python:3.11-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia e instala as dependências primeiro (melhora cache)
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copia o restante da aplicação
COPY . .

# Define o caminho para permitir importações absolutas
ENV PYTHONPATH=/app

# Exposição da porta (opcional, mas ajuda no mapeamento)
EXPOSE 8000

# Comando de inicialização da API
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]






