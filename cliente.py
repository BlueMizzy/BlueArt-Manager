from logging import INFO
import os
from time import sleep
import utils, menu, comissao, config, arquivo

def add_cliente():
    clientes = config.verifica_arquivo('clientes.json', 'clientes')

    while True:                     #loop para adicionar clientes
        print()
        print('\n--- ADICIONAR NOVO CLIENTE ---')
        nome = input('Nome do cliente (ou "sair"): ').capitalize().strip()

        if nome.lower() == 'sair':
            break

        sexo = input('Sexo (F/M): ').capitalize().strip()
        if sexo not in 'FM':
            print('Tente npvamente.')
            sexo = input()

        idade = int(input('idade: '))
        if idade < 18:
            print('Por favor, informe o número do seu responsável.')

        celular = input('Numero de celular: ')
        email = input('Email: ').capitalize().strip()
        cidade = input('Cidade: ').capitalize().strip()

        opcao, confirm = comissao.add_comissao(nome)
        stts = comissao.status_padrao()
        
        if confirm == 'S':
            print(f'Cliente {nome} adicionado com sucesso!')
        
            clientes[nome] = {
                'sexo': sexo,
                'idade': idade,
                'celular': celular,
                'email': email,
                'cidade': cidade,
                'opcao': opcao,
                'status': stts,
                'data': utils.data(),
                'hora': utils.hora()
        }

            arquivo.salvar_json('clientes.json', clientes)

            print()
            print('>>> Cliente adicionado!')
            print(f'Agora temos {len(clientes)} clientes cadastrados.')
            return clientes

        else:
            print('Cliente não adicionado. Voltando ao menu principal...')
            sleep(2)
            return menu.menu_principal()


                            # lista todos os clientes cadastrados no arquivo clientes.json
def listar_clientes(clientes):
    print('\n--- LISTA DE CLIENTES ---')

    dicio = arquivo.ler_json(clientes)

    for nome, info in dicio.items():
        exibir_dados_cliente(nome, dicio)



def editar_cliente(clientes):
    print('\n--- EDITAR CLIENTE ---')

    dicio = arquivo.ler_json(clientes)
        
    nome = input('Digite o nome do cliente que deseja encontrar: ').capitalize().strip()

    if nome in dicio:
        print(f'Cliente encontrado!')

        print()
        print('>>> INFORMAÇÕES ATUAIS')
        print()

        exibir_dados_cliente(nome, dicio)

        print()
        print('Digite sua escolha: - nome, - sexo, - idade, - celular, - email, - cidade: ',sep=',')
        campo = input().lower().strip()

        if campo in dicio[nome]:
            novo_valor = input(f'Novo valor para {campo}: ')
            dicio[nome][campo] = novo_valor

            arquivo.salvar_json('clientes.json', dicio)



def pesquisar_cliente(clientes):
    print('\n--- PESQUISAR CLIENTE ---')

    dicio = arquivo.ler_json(clientes)

    nome = input('Pesquisar: ').capitalize().strip()
    print()
    if nome in dicio:
        for i, j in dicio[nome].items():
            print(f'{i.capitalize()}: {j}')
            sleep(1)
    else:
        print('Cliente não encontrado.')



def excluir_cliente(clientes):
    print('\n--- EXCLUIR CLIENTE ---')

    dicio = arquivo.ler_json(clientes)

    nome = input('Excluir o cliente: ').capitalize().strip()

    if nome in dicio:
        confirmacao = input(f'Tem certeza que deseja excluir {nome}? (S/N): ').strip().upper()

        if confirmacao == 'S':
            del dicio[nome]
            print(f'Cliente {nome} excluído com sucesso.')

            arquivo.salvar_json('clientes.json', dicio)

        else:
            print('Exclusão cancelada.')


def exibir_dados_cliente(nome, info):
    print(f'Nome: {nome}')
    print(f'Sexo: {info[nome]["sexo"]}')
    print(f'idade: {info[nome]["idade"]}')
    print(f'Celular: {info[nome]["celular"]}')
    print(f'Email: {info[nome]["email"]}')
    print(f'Cidade: {info[nome]["cidade"]}')
    print('-' * 30)
    