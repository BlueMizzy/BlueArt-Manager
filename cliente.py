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

        opcao, confirm = comissao.add_comissao(nome) 
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
            print(f'Agora temos {len(clientes)} clientes cadastrados.')
            return clientes  

        else:
            print('Cliente não adicionado. Voltando ao menu principal...')
            sleep(2)
            return


                            # lista todos os clientes cadastrados no arquivo clientes.json
def listar_clientes(clientes):
    print('\n--- LISTA DE CLIENTES ---')

    dicio = arquivo.ler_json(clientes)

    for nome, info in dicio.items():
        utils.exibir_dados_cliente(nome, dicio)



def editar_cliente(clientes):
    print('\n--- EDITAR CLIENTE ---')

    dicio = arquivo.ler_json(clientes)
        
    nome = input('Nome do cliente que deseja encontrar: ').capitalize().strip()

    if nome in dicio:
        print(f'Cliente encontrado!\n')
        print('>>> INFORMAÇÕES ATUAIS\n')

        utils.exibir_dados_cliente(nome, dicio)

        print('\nDigite sua escolha: - nome, - sexo, - idade, - celular, - email, - cidade: ',sep=',')
        campo = input().lower().strip()

        if campo in dicio[nome]:        #muda o valor antigo para o novo valor.
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

    