import os

restaurantes = [{'nome':'Bananas Shop', 'categoria':'frutas','ativado':False},
                {'nome':'Kaozone', 'categoria':'salgados','ativado':True}]

def exibir_nome_programa(): 
    print('Sabor Express\n')

def voltar():
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()

def exibir_opcoes(): 
    print('1.Cadastrar Restaurante')
    print('2.Listar Restaurante')
    print('3.Alternar Estado do Restaurante')
    print('4.Sair\n')

def exibir_subtitulo(subtitulo):
    os.system('cls')
    linha = '*' * (len(subtitulo))
    print(linha)
    print(subtitulo)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    exibir_subtitulo("CADASTRO DE NOVOS RESTAURANTES")
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
    dados_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativado':False}
    restaurantes.append(dados_restaurante)
    print(f'O restaurante "{nome_do_restaurante}" foi cadastrado com sucesso!\n')
    voltar()

def listar_restaurantes():
    exibir_subtitulo("LISTANDO OS RESTAURANTES: ")

    print(f'NOME DO RESTAURANTE'.ljust(22),'| CATEGORIA'.ljust(22), '| STATUS')
    for restaurante in restaurantes:
        nome = restaurante['nome']
        categoria = restaurante['categoria']
        ativado = 'Ativado' if restaurante['ativado'] else 'Desativado'
        
        print(f'- {nome.ljust(20)} | {categoria.ljust(20)} | {ativado}')
    voltar()

def alternar_estado_restaurante(): 
    exibir_subtitulo('Alterando Estado do Restaurante: ')
    #Restaurante 
    nome = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativado'] = not restaurante['ativado']
            mensagem = f'O restaurante {nome} foi ativado com com sucesso' if restaurante['ativado'] else f'o restaurante {nome} foi desativado com sucesso'
            print(mensagem)  
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')

    voltar()

def finalizar_app(): 
    exibir_subtitulo("ENCERRANDO APLICAÇÃO...")    

def opcao_invalida():
    print('Opção inválida!\n')
    voltar()

def escolher_opcao(): 
    try: 
        opcao_escolhida = input('Escolha uma opção: ')
        opcao_escolhida = int(opcao_escolhida)

        if opcao_escolhida == 1 :
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2 :
            listar_restaurantes()
        elif opcao_escolhida == 3 :
            alternar_estado_restaurante()
        elif opcao_escolhida == 4 :
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()
    

def main():
    os.system('cls')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()