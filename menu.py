from time import sleep
import cliente, faturamento, status, utils

def menu_principal():
    opcoes = {
        '1': 'Menu de Clientes',
        '2': 'Menu de Comissões',
        '3': 'Menu de Faturamento',
        '4': 'Menu de Configuração',
        '0': 'Encerrar'
    }

    while True:
        op = utils.criar_menu('BLUEART MANAGER', opcoes)

        if op == '0':
            print('Encerrando...')
            sleep(2)
            break

        match op:
            case '1':
                menu_clientes()

            case '2':
                menu_comissao()

            case '3':
                menu_faturamento()

            case '4':
                print('Em desenvolvimento.')


def menu_clientes():
    opcoes = {
        '1': 'Adicionar',
        '2': 'Listar',
        '3': 'Editar',
        '4': 'Pesquisar',
        '5': 'Excluir',
        '0': 'Sair'
    }

    while True:
        op = utils.criar_menu('CLIENTES', opcoes)

        if op == '0':
            print('Voltando...')
            sleep(2)
            return

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
    opcoes = {
        '1': 'Comissões em andamento',
        '2': 'Comissões pendentes',
        '3': 'Comissões finalizadas',
        '4': 'Comissões canceladas',
        '5': 'Mudar status',
        '0': 'Voltar ao menu principal'
    }

    while True:
        op = utils.criar_menu('COMISSÕES', opcoes)

        if op == '0':
            print('Voltando...')
            sleep(2)
            return
        

        match op:
            case '1':
                status.listar_comissoes_por_status('Em andamento')

            case '2':
                status.listar_comissoes_por_status('Pendente')

            case '3':
                status.listar_comissoes_por_status('Finalizada')

            case '4':
                status.listar_comissoes_por_status('Cancelada')

            case '5':
                status.mudar_status_comissao()


def menu_faturamento():
    opcoes = {
        '1': 'Faturamento do dia',
        '2': 'Faturamento do mês',
        '0': 'Voltar ao menu principal'
    }


    while True:
        op = utils.criar_menu('FATURAMENTO', opcoes)

        if op == '0':
            print('Voltando...')
            return

        match op:
            case '1':
                faturamento.faturamento_dia()
                
            case '2':
                faturamento.faturamento_mes()


def menu_configuracao():
    pass
