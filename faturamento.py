import arquivo
from datetime import datetime

def faturamento_dia():
    print('\n--- FATURAMENTO DO DIA ---')

    dicionario = arquivo.ler_json('clientes.json')

    dia = datetime.now().strftime('%d/%m/%Y')
    soma_faturamento = 0.0
 
    for nome, info in dicionario.items():
        if info["data"] == dia and info["status"] == 'Finalizada':
            soma_faturamento += info['opcao']['brl']

    print(f'Faturamento do dia {dia}: R$ {soma_faturamento:.2f}')



def faturamento_mes():
    print('\n--- FATURAMENTO DO MÊS ---')

    dicionario = arquivo.ler_json('clientes.json')

    mes = datetime.now().strftime('%m/%Y')
    soma_faturamento = 0.0

    for nome, info in dicionario.items():
        if info["data"][3:] == mes and info["status"] == 'Finalizada':
            soma_faturamento += info['opcao']['brl']

    print(f'Faturamento do mês {mes}: R$ {soma_faturamento:.2f}')



def menu_faturamento():
    tam = 40

    opcoes = {
        '1': 'Faturamento do dia',
        '2': 'Faturamento do mês',
        '0': 'Voltar ao menu principal'
    }


    while True:
        print(f'+{"-" * tam}+')
        print(f'|{"FATURAMENTO":^{tam}}|')
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
                faturamento_dia()
                
            case '2':
                faturamento_mes()
            
                

            