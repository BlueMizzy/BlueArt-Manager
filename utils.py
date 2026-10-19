import os
from datetime import datetime

def limpar_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def data():
    agora = datetime.now()
    return agora.strftime('%d/%m/%Y')                  # diz a data do registro da comissão

def hora():
    agora = datetime.now()
    return agora.strftime('%H:%M')                     # diz a hora do registro da comissão


def exibir_dados_cliente(nome, info):
    print(f'Nome: {nome}')
    print(f'Sexo: {info[nome]["sexo"]}')
    print(f'idade: {info[nome]["idade"]}')
    print(f'Celular: {info[nome]["celular"]}')
    print(f'Email: {info[nome]["email"]}')
    print(f'Cidade: {info[nome]["cidade"]}')
    print('-' * 30)


def criar_menu(titulo, opcoes, tam=40):
    while True:
        print(f'+{"-" * tam}+')
        print(f'|{titulo:^{tam}}|')
        print(f'+{"-" * tam}+')

        for numero, descricao in opcoes.items():
            print(f'|{f'{numero} - {descricao}':<{tam}}|')

        print(f'+{"-" * tam}+')

        op = input("Escolha: ")

        if op in opcoes:
            return op

        print('Opção inválida.')