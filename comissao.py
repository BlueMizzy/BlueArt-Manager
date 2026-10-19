from time import sleep
import arquivo

#essa função é chamada pelo add cliente, lista as opções e retorna as respostas
def add_comissao(cliente):
    print(f'\nQual opção o(a) {cliente} decidiu? ')
    print()

    dados = arquivo.ler_json('artes.json')
    
    for i, j in dados.items():
        print(f'{i} - {j}')

    while True:
        opcao = input('Escolha: ')

        if opcao not in dados:
            print('Não existe essa opção.')

        else: 
            estilo = dados.get(opcao)
            print(f'Ele(a) escolheu {estilo}.\n')
            resposta = input('Deseja confirmar esta opção? [S/N]: ').strip().upper()

            return estilo, resposta


def estilo_arte(artes):     
    proximo_numero = len(artes) + 1

    print('Estilo de arte. ("0" para finalizar): \n')
    print('Ex: Realismo, Retrato estilizado, etc.')

    while True:
        arte = input().capitalize().strip()

        if arte == '0':
            print('Salvando...')
            sleep(2)
            break

        artes[str(proximo_numero)] = arte
        proximo_numero += 1

    arquivo.salvar_json('artes.json', artes)

    return artes