import arquivo
from datetime import datetime

def faturamento_dia():
    print('\n--- FATURAMENTO DO DIA ---')

    dicio = arquivo.ler_json('clientes.json')

    dia = datetime.now().strftime('%d/%m/%Y')
    sum = 0.0
 
    for nome, info in dicio.items():
        if info["data"] == dia and info["status"] == 'Finalizada':
            sum += info['opcao']['brl']

    print(f'Faturamento do dia {dia}: R$ {sum:.2f}')


def faturamento_mes():
    print('\n--- FATURAMENTO DO MÊS ---')

    dicio    = arquivo.ler_json('clientes.json')

    mes = datetime.now().strftime('%m/%Y')
    sum = 0.0

    for nome, info in dicio.items():
        if info["data"][3:] == mes and info["status"] == 'Finalizada':
            sum += info['opcao']['brl']

    print(f'Faturamento do mês {mes}: R$ {sum:.2f}')
