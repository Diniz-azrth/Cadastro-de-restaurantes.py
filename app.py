import os
restaurantes = []

def exibir_nome_do_programa():
    print ('''𝖘𝖆𝖇𝖔𝖗 𝖊𝖝𝖕𝖗𝖊𝖘𝖘\n''')
    # https://fsymbols.com/

def exibir_opcoes():
    print ("1. Cadrastar restaurante")
    print ("2. Listar restaurantes")
    print ("3. Ativar restaurante")
    print ("4. Desativar restaurante")
    print ("5. Sair")

def escolher_opcoes():
    try:
        opcao_escolhida = int(input('\nEscolha uma opção: '))
        match opcao_escolhida:
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                ativar_restaurante()
            case 4:
                destivar_restaurante()
            case 5:
                finalizar_app()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()

def finalizar_app():
    os.system("cls")
    print("Finalizando o app")

def main():
    os.system("cls")
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()

def voltar_ao_menu_principal():
    input ('\nPressione enter voltar ao menu principal')
    main()

def inicializar(texto):
    os.system('cls')
    print(f'{texto}\n')

def opcao_invalida():
    print('Opção invalida\n')
    voltar_ao_menu_principal()

def cadastrar_novo_restaurante():
    inicializar('Cadrasto de novos restaurantes')
    nome_restaurante = input("Digite o nome do restaurante: ")
    categoria_restaurante = input(f"Digite a categoria do restaurante {nome_restaurante}: ")
    infos_restaurante = {'nome' : nome_restaurante, 'categoria' : categoria_restaurante, 'status' : False}
    restaurantes.append(infos_restaurante)
    print(f'O restaurante {nome_restaurante} foi cadrastado com sucesso!')
    voltar_ao_menu_principal()

def listar_restaurantes():
    inicializar('Lista de restaurantes')

    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | {'Status'}')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        status_restaurante = "Ativado" if restaurante['status'] else "Desativado"
        print(f'• {nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {status_restaurante}')
    voltar_ao_menu_principal()

def ativar_restaurante():
    inicializar('Ativar restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja ativar: ')
    encontrado = False

    for restaurante in restaurantes:
        if restaurante['nome'] == nome_restaurante:
            encontrado = True
            if restaurante['status']:
                print(f'O restaurante {restaurante['nome']} já está ativo')
            else:
                restaurante['status'] = True
                print(f'O restaurante {restaurante['nome']} foi ativado com sucesso!')
        
    if not encontrado:
         print ('Restaurante não encontrado')

    voltar_ao_menu_principal()

def destivar_restaurante():
    inicializar('Desativar restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja desativar: ')
    encontrado = False

    for restaurante in restaurantes:
        if restaurante['nome'] == nome_restaurante:
            encontrado = True
            if restaurante['status']:
                restaurante['status'] = False
                print(f'O restaurante {restaurante['nome']} foi desativado com sucesso!')
            else:
                print('O restaurante já está desativado')
    
    if not encontrado:
         print ('Restaurante não encontrado')

    voltar_ao_menu_principal()

if __name__ == "__main__":
    main()