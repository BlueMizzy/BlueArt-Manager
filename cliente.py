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
        print(f'Nome: {nome}')
        print(f'Sexo: {info["sexo"]}')
        print(f'Idade: {info["idade"]}')
        print(f'Celular: {info["celular"]}')
        print(f'Email: {info["email"]}')
        print(f'Cidade: {info["cidade"]}')
        print('-' * 30)



def editar_cliente(clientes):
    print('\n--- EDITAR CLIENTE ---')

    dicio = arquivo.ler_json(clientes)
        
    nome = input('Digite o nome do cliente que deseja encontrar: ').capitalize().strip()

    if nome in dicio:
        print(f'Cliente encontrado: {nome}')

        print()
        print('>>> INFORMAÇÕES ATUAIS')
        print()

        print(f'Nome: {nome}')
        print(f'Sexo: {dicio[nome]["sexo"]}')
        print(f'idade: {dicio[nome]["idade"]}')
        print(f'Celular: {dicio[nome]["celular"]}')
        print(f'Email: {dicio[nome]["email"]}')
        print(f'Cidade: {dicio[nome]["cidade"]}')

        print()
        campo = input('Digite sua escolha: \n- nome \n- sexo \n- idade \n- celular \n- email \n- cidade: ').lower().strip() #mexer nisso aqui para ficar mais bonito e organizado

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

