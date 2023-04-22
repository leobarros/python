import requests
import threading

# Função para fazer uma solicitação HTTP usando a biblioteca requests
def fazer_requisicao(url):
    response = requests.get(url)
    print(f'Resposta de {url}: {response.status_code}')

# Função para ler as URLs de um arquivo
def ler_urls_de_arquivo(arquivo):
    with open(arquivo, 'r') as f:
        urls = f.readlines()
    urls = [url.strip() for url in urls]  # Remove os caracteres de quebra de linha e espaços em branco
    return urls

# Lista de arquivos que contêm as URLs
arquivos = ['arquivo_1.txt', 'arquivo_2.txt', 'arquivo_3.txt']

# Lista para armazenar as URLs de todos os arquivos
urls_totais = []

# Lê as URLs de cada arquivo e as adiciona à lista de URLs totais
for arquivo in arquivos:
    urls = ler_urls_de_arquivo(arquivo)
    urls_totais.extend(urls)

# Cria uma lista de threads
threads = []
for url in urls_totais:
    # Cria uma nova thread para cada URL e inicia-a
    t = threading.Thread(target=fazer_requisicao, args=(url,))
    t.start()
    threads.append(t)

# Aguarda todas as threads terminarem
for t in threads:
    t.join()

print('Todas as solicitações foram concluídas.')
