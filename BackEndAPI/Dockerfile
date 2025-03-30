# Usar uma imagem do Python
FROM python:3.10

# Definir o diretório de trabalho no container
WORKDIR /app

# Copiar os arquivos do backend para o container
COPY . /app

# Instalar as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expor a porta do FastAPI
EXPOSE 8000

# Comando para rodar o FastAPI
CMD ["uvicorn", "BackEndAPI.FastAPITest:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
