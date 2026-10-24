import arquivo
from time import sleep
from pathlib import Path

def analise():
    artes = arquivo.verifica_arquivo('artes.json', 'artes')
    print('--- CONFIGURAÇÃO ESTILOS DE ARTE ---\n')
    while True:
        if not artes: 
            estilo = estilo_arte(artes)
        else:
            print('> Você já tem estilos salvos.')
            escolha = input('Quer adicionar mais? [S/N]: ').upper().strip()
            print()

            if escolha == 'N':
                print('Okay!')
                sleep(2)
                break
                
                
            elif escolha == 'S':
                estilo = estilo_arte(artes)
                
            else:
                print('Resposta inválida.')


def Artista():      # Pega os dados do usuario e coloca em um dicionário
    
    dados = arquivo.verifica_arquivo('artista.json', 'artista')

    if not dados:
        print('--- DADOS DO ARTISTA ---\n')
        nome = input('Nome: ').capitalize().strip()
        nome_exibicao = input('Nome de exibição: ').strip()
        email = input('Email: ').strip()
        print()

        dados = {
            'nome': nome,
            'nome_exibicao': nome_exibicao,
            'email': email
        }

        arquivo.salvar_json('artista.json', dados)
        print('Dados salvos!\n')
        print(f'seja bem vindo(a) {dados['nome_exibicao']}')
        sleep(3)
        
    else:
        print(f'>>> Bem vindo(a) de volta {dados['nome_exibicao']}! <<<'.upper())
        sleep(2)

    return dados


def editar_dados_artista():
    print('\n--- EDITAR CONFIGURAÇÃO DO ARTISTA ---')
    
    artista = arquivo.ler_json('artista.json')

    print('\nEscolha qual campo editar: \n- Nome \n- Nome de exibição \n- email:')
    campo = input().strip()

    if campo in artista:
        novo_valor = input(f'Novo valor para {campo}')
        artista[campo] = novo_valor
        arquivo.salvar_json('artista.json', artista)
        print(f'Você mudou seu {campo} para {novo_valor}')
    else:
        print(f'{campo} não encontrado.')


def estilo_arte(artes):     
    proximo_numero = len(artes) + 1

    print('Estilo de arte. ("0" para finalizar): ')
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


def excluir_conta():
    print(
        'Tem certeza que deseja excluir essa conta? '
        'Essa ação não pode ser desfeita. [S/N]'
    )

    while True:
        resposta = input().upper().strip()

        if resposta == 'N':
            print('Exclusão cancelada.')
            return
        
        elif resposta == 'S':
            pasta_dados = Path(__file__).resolve().parent
            arquivos_da_conta = (
               'artes.json',
               'clientes.json',
               'artista.json'
            )

            for nome_arquivo in arquivos_da_conta:
               caminho = pasta_dados / nome_arquivo
               if caminho.exists():
                   caminho.unlink()

            print('Conta excluída com sucesso!')
            return

        else:
            print('Resposta inválida.Digite S ou N.')
