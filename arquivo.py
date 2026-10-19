import json, os
from time import sleep


def salvar_json(nome_arquivo, dados):                                   # Salva em Json
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)



def ler_json(nome_arquivo):                          # Lê qualquer arquivo json
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        dicio = json.load(arquivo)
        return dicio


def verifica_arquivo(nome_arquivo, nome_dicio):     # Ve se o arquivo chamado existe
    if os.path.exists(nome_arquivo):            
        nome_dicio = ler_json(nome_arquivo)
        return nome_dicio
    else:
        nome_dicio = {}
        sleep(2)
        return nome_dicio
