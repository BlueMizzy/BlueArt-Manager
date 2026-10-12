from time import sleep
import cliente
import comissao
import faturamento

# Cara ta muito repetitivo ainda, não sei fazer uma função generica para fazer menus. Vou fazer assim por enquanto e depois eu aprendo.

def menu_principal():
    tam = 40

    opcoes = {
        '1': 'Menu de Clientes',
        '2': 'Menu de Comissões',
        '3': 'Menu de Faturamento',
        '4': 'Menu de Configuração',
        '0': 'Sair'
    }
# É a refatoração dos menus, repeti a base em todos eles. Um dia eu mudo.

    while True:
        print(f'+{"-" * tam}+')
        print(f'|{"BLUEART MANAGER":^{tam}}|')
        print(f'+{"-" * tam}+')

        for i, j in opcoes.items():
            print(f'|{f" {i} - {j}":<{tam}}|')         # centralizar a esquerda no espaço definido pela variavel tam
        print(f'+{"-" * tam}+')

        op = input("Escolha: ")

        if op not in opcoes:
            print('Opção inválida')
            continue

        if op == '0':
            break

        print(f'>>> {opcoes[op]}\n')

        match op:
            case '1':
                menu_clientes()

            case '2':
                menu_comissao()

            case '3':
                faturamento.menu_faturamento()


def menu_clientes():
    tam = 40

    opcoes = {
        '1': 'Adicionar',
        '2': 'Listar',
        '3': 'Editar',
        '4': 'Pesquisar',
        '5': 'Excluir',
        '0': 'Sair'
    }


    while True:
        print(f'+{"-" * tam}+')
        print(f'|{"CLIENTES":^{tam}}|')
        print(f'+{"-" * tam}+')

        for i, j in opcoes.items():
            print(f'|{f" {i} - {j}":<{tam}}|')
        print(f'+{"-" * tam}+')

        op = input("Escolha: ")

        if op not in opcoes:
            print('Opção inválida')
            continue

        if op == '0':
            break

        print(f'>>> {opcoes[op]}\n')

        match op:
            case '1':
                cliente.add_cliente()

            case '2':
                cliente.listar_clientes('clientes.json')

            case '3':
                cliente.editar_cliente('clientes.json')

            case '4':
                cliente.pesquisar_cliente('clientes.json')

            case '5':
                cliente.excluir_cliente('clientes.json')
                

def menu_comissao():
    tam = 40

    opcoes = {
        '1': 'Comissões em andamento',
        '2': 'Comissões pendentes',
        '3': 'Comissões finalizadas',
        '4': 'Comissões canceladas',
        '5': 'Mudas status',
        '0': 'Voltar ao menu principal'
    }


    while True:
        print(f'+{"-" * tam}+')
        print(f'|{"COMISSÕES":^{tam}}|')
        print(f'+{"-" * tam}+')

        for i, j in opcoes.items():
            print(f'|{f" {i} - {j}":<{tam}}|')
        print(f'+{"-" * tam}+')

        op = input("Escolha: ")

        if op not in opcoes:
            print('Opção inválida')
            continue

        if op == '0':
            print('Voltando...')
            break

        print(f'>>> {opcoes[op]}\n')

        match op:
            case '1':
                comissao.listar_comissoes_por_status('Em andamento')

            case '2':
                comissao.listar_comissoes_por_status('Pendente')

            case '3':
                comissao.listar_comissoes_por_status('Finalizada')

            case '4':
               comissao.listar_comissoes_por_status('Cancelada')

            case '5':
                comissao.mudar_status_comissao()

    