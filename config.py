import arquivo, comissao
from time import sleep

def analise():
    artes = arquivo.verifica_arquivo('artes.json', 'artes')
    print('--- CONFIGURAÇÃO ESTILOS DE ARTE ---\n')

    if not artes: 
        estilo = comissao.estilo_arte(artes)
    else:
        escolha = input('Quer adicionar mais? [S/N]: ').upper().strip()
        print()

        if escolha == 'N':
            print('Okay!')
            sleep(2)
            
        elif escolha == 'S':
            estilo = comissao.estilo_arte(artes)



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
        sleep(3)

    return dados


def editar_dados_artista():
    print('\n--- EDITAR CONFIGURAÇÃO DO ARTISTA ---')
    
    artista = arquivo.ler_json('artista.json')

    print('\nEscolha qual campo editar: - Nome, - Nome de exibição, - email:', sep=',')
    campo = input().strip()

    if campo in artista:
        novo_valor = input(f'Novo valor para {campo}')
        artista[campo] = novo_valor
        arquivo.salvar_json('artista.json', artista)

    print(f'Você mudou seu {campo} para {novo_valor}')
