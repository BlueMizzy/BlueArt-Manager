from time import sleep
import arquivo

def status_padrao():
    stts = 'Em andamento'  # Valor padrão para status de comissão
    return stts


def mudar_status_comissao():
    print('\n--- MUDAR STATUS DA COMISSÃO ---')

    dicio = arquivo.ler_json('clientes.json')

    nome = input('Nome do cliente: ').capitalize().strip()

    if nome in dicio:
        cliente_info = dicio[nome]

        print(f'Cliente: {nome}')   #mostrar apenas informações escolhidas
        # R${cliente_info["opcao"]["brl"]:.2f}') adicionar isso como opcional para ser colocado no dict do cliente pelo editar cliente
        print(f'Status atual: {cliente_info["status"]}')

        print('\nNovo status:')

        status = int(input('[1] Em andamento\n[2] Pendente\n[3] Finalizada\n[4] Cancelada\nDigite o número correspondente: '))


        if status == 1:
            cliente_info['status'] = 'Em andamento'

        elif status == 2:
            cliente_info['status'] = 'Pendente'

        elif status == 3:
            cliente_info['status'] = 'Finalizada'

        elif status == 4:
            cliente_info['status'] = 'Cancelada'
            
        else:
            print('Opção inválida. Voltando ao menu principal....')
            sleep(2)
            return 

        print(f'Status da comissão do cliente {nome} alterado para: {cliente_info["status"]}')

        arquivo.salvar_json('clientes.json', dicio)

    else:
        print(f'Cliente {nome} não encontrado. Voltando ao menu principal....')
        sleep(2)
        return


def listar_comissoes_por_status(status):
    print(f'\n--- LISTA DE COMISSÕES {f"{status}".upper()} ---')

    dicio = arquivo.ler_json('clientes.json')

    comissao_filtrada = {
        nome: info

        for nome,info in dicio.items()
        if info.get('status') == status
    }

    for nome, info in comissao_filtrada.items():
        print(f'Nome do Cliente: {nome}')
        # colocar futuramente o preco e a descrição que o proprio artista fará
    print(f'\nTotal de comissões {status}: {len(comissao_filtrada)}')