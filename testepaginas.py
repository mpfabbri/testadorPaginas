import requests
import os
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
def gerar_relatorio(urls):
    relatorio = "Relatório de Disponibilidade de URLs\n"
    relatorio += "=" * 40 + "\n"
    for url in urls:
        status = verificar_disponibilidade(url)
        relatorio += f"{url}: {status}\n"
    return relatorio

# Obter data e hora atuais
data_hora_atual = datetime.now().strftime("%Y%m%d_%H%M%S")

# Definir pasta e nome do arquivo
pasta = "/home/mpfabbri/Documentos/Projetos/testadorPaginas"  # Substitua pelo caminho desejado
nome_arquivo = f"relatorioDisponibilidade_{data_hora_atual}.txt"
caminho_completo = os.path.join(pasta, nome_arquivo)

# Executar e imprimir o relatório
relatorio = gerar_relatorio(urls)
print(relatorio)

# Salvar o relatório em um arquivo na pasta especificada
os.makedirs(pasta, exist_ok=True)  # Cria a pasta se não existir
with open(caminho_completo, "w") as file:
    file.write(relatorio)

print(f"Relatório salvo em: {caminho_completo}")
