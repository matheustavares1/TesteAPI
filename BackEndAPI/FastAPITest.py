import csv

from fastapi import FastAPI, Query
from fuzzywuzzy import process
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],  # Permite requisições do Vue.js
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permite todos os cabeçalhos
)
# Função para carregar dados do CSV
def carregar_operadoras():
    operadoras = []
    with open('Relatorio_cadop.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')  # Ajusta para o delimitador correto
        for row in reader:
            operadoras.append({
                'Registro_ANS': row['Registro_ANS'],
                'CNPJ': row['CNPJ'],
                'Razao_Social': row['Razao_Social'],
                'Nome_Fantasia': row['Nome_Fantasia'],
                'Modalidade': row['Modalidade'],
                'Cidade': row['Cidade'],
                'UF': row['UF'],
                'Telefone': row['Telefone']
            })
    return operadoras

@app.get("/buscar-operadoras")
def buscar_operadoras(termo: str = Query(..., description="Termo de busca")):
    operadoras = carregar_operadoras()
    resultados = process.extract(termo, [op["Nome_Fantasia"] for op in operadoras], limit=5)
    operadoras_encontradas = [op for op in operadoras if op["Nome_Fantasia"] in [r[0] for r in resultados]]
    return {"resultados": operadoras_encontradas}

