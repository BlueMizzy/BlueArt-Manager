from logging import INFO
from time import sleep
import utils, comissao, config, arquivo, status

def add_cliente():
    clientes = arquivo.verifica_arquivo('clientes.json', 'clientes')

    while True:                     #loop para adicionar clientes
        print()
        print('\n--- ADICIONAR NOVO CLIENTE ---')
        nome = input('Nome do cliente (ou "sair"): ').capitalize().strip()

        if nome.lower() == 'sair':
            break

        email = input('Email: ').capitalize().strip()

        #chama a função add comissão para fazer as perguntas e guardar as respostas nas duas variaveis.

        opcao, confirm = comissao.mostrar_opcao(nome) 
        stts = status.status_padrao()         #stts padrão 'em andamento'
        
        if confirm == 'S':
            clientes[nome] = {
                'email': email,
                'opcao': opcao,
                'status': stts,
                'data': utils.data(),
                'hora': utils.hora()
        }

            arquivo.salvar_json('clientes.json', clientes)

            print()
            print('>>> Cliente adicionado!')
            print(f'Agora temos {len(clientes)} clientes cadastrados.\n')
            return clientes  

        else:
            print('Cliente não adicionado. Voltando ao menu principal...\n')
            sleep(2)
            return


                            # lista todos os clientes cadastrados no arquivo clientes.json
def listar_clientes(clientes):
    print('\n--- LISTA DE CLIENTES ---')

    dicio = arquivo.ler_json(clientes)

    for nome, info in dicio.items():
        utils.exibir_dados_cliente(nome, info)
        


def editar_cliente(clientes):
    print('\n--- EDITAR CLIENTE ---')

    dicio = arquivo.ler_json(clientes)
    nome = input('Nome do cliente que deseja encontrar: ').capitalize().strip()

    if nome in dicio:
        print(f'Cliente encontrado!\n')
        print('>>> INFORMAÇÕES ATUAIS')
        utils.exibir_dados_cliente(nome, dicio[nome])

        print('\nVocê pode adicionar novos campos ou editar os antigos.\n')
        print('Ex: descricao: O cliente quiz um semi realismo de corpo inteiro,personagem adicional...')

        print('\n>> Digite sua escolha:')
        campo = input().lower().strip()
     
        if campo in dicio[nome]:       #muda o valor antigo para o novo valor.
            novo_valor = input(f'Novo valor para {campo}: ')
            dicio[nome][campo] = novo_valor
            arquivo.salvar_json('clientes.json', dicio)

        if campo not in dicio[nome]:
            print('\nDeseja adicionar esse campo a esse cliente? [S/N]')
            resposta = input().strip().upper()

            if resposta == 'N':
                print('\nOkay.')

            elif resposta =='S':
                print('\nConteúdo:')
                valor = input()
                dicio[nome][campo] = valor
                arquivo.salvar_json('clientes.json', dicio)
            else:

                print('Desculpe. Tente novamente.')
    else:
        print('Cliente não encontrado.')


def pesquisar_cliente(clientes):
    print('\n--- PESQUISAR CLIENTE ---')

    dicio = arquivo.ler_json(clientes)

    nome = input('Pesquisar: ').capitalize().strip()
    print()
    if nome in dicio:
        for i, j in dicio[nome].items():
            print(f'{i}: {j}')
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

