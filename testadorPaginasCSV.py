import requests
import os
import csv
from datetime import datetime

# Lista de URLs para verificar
urls = [
    "https://www.google.com",
    "https://www.microsoft.com",
    "https://www.nonexistentwebsite.com"
]

# Função para verificar a disponibilidade de uma URL
def verificar_disponibilidade(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return "Disponível"
        else:
            return f"Indisponível (Status Code: {response.status_code})"
    except requests.exceptions.RequestException as e:
        return f"Indisponível (Erro: {e})"

# Gerar relatório
def gerar_relatorio_csv(urls, caminho_arquivo):
    with open(caminho_arquivo, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["URL", "Status", "Data e Hora"])
        for url in urls:
            status = verificar_disponibilidade(url)
            data_hora_atual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            writer.writerow([url, status, data_hora_atual])

# Obter data e hora atuais para o nome do arquivo
data_hora_atual = datetime.now().strftime("%Y%m%d_%H%M%S")

# Definir pasta e nome do arquivo
pasta = "/home/mpfabbri/Documentos/Projetos/testadorPaginas/Relatorios"  # Substitua pelo caminho desejado
nome_arquivo = f"relatorioDisponibilidade_{data_hora_atual}.csv"
caminho_completo = os.path.join(pasta, nome_arquivo)

# Criar a pasta se não existir
os.makedirs(pasta, exist_ok=True)

# Gerar e salvar o relatório CSV
gerar_relatorio_csv(urls, caminho_completo)

print(f"Relatório salvo em: {caminho_completo}")
