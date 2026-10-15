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
