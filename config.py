import json, os, arquivo
from time import sleep
def opcao_commBR():                         # Opções de tamanho, pintura e tipo de arte
    comm = [{'tipo': 'Sketch', 'tamanho': 'Busto', 'brl': 15.00}, {'tipo': 'Sketch', 'tamanho': 'Half body', 'brl': 35.00}, 
    {'tipo': 'Sketch', 'tamanho': 'Full body', 'brl': 60.00}, {'tipo': 'Flat color', 'tamanho': 'Busto', 'brl': 30.00},
    {'tipo': 'Flat color', 'tamanho': 'Half body', 'brl': 50.00}, {'tipo': 'Flat color', 'tamanho': 'Full body', 'brl': 75.00},
    {'tipo': 'Full render', 'tamanho': 'Busto', 'brl': 50.00}, {'tipo': 'Full render', 'tamanho': 'Half body', 'brl': 80.00},
    {'tipo': 'Full render', 'tamanho': 'Full body', 'brl': 120.00}]
    return comm


def verifica_arquivo(nome_arquivo, nome_dicio):     # Ve se o arquivo chamado existe
    if os.path.exists(nome_arquivo):            
        nome_dicio = arquivo.ler_json(nome_arquivo)
    
        print(f'--- Arquivo encontrado! ---\n')
        return nome_dicio
    else:
        nome_dicio = {}
        print('>>> Nenhum arquivo encontrado. Criando arquivo...\n')
        sleep(2)

        return nome_dicio


def Artista():      # Pega os dados do usuario e coloca em um dicionário
    
    dados_artista = verifica_arquivo('artista.json', 'artista')

    if not dados_artista:
        print('--- DADOS DO ARTISTA ---\n')
        nome = input('Nome: ').capitalize().strip()
        idade = int(input('Idade: '))

        dados_artista = {
            'nome': nome,
            'idade': idade
        }

        arquivo.salvar_json('artista.json', dados_artista)
        print('Dados salvos!')
        
    else:
        print(f'Bem vindo(a) de volta {dados_artista['nome']}!')
        sleep(3)

    return dados_artista
