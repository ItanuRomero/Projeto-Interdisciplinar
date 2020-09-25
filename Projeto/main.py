import menu_functions as menu
import interface
import database as bd
bd.createBanco('bd_pinatalk.db')
bd.inserirCategoria('bd_pinatalk.db')
# interface.limpa_tela()
while True:
    option_user = menu.create_menu()
    if option_user == 1:
        print(option_user)
        # segue fluxo
    elif option_user == 2:
        print(option_user)
        # segue fluxo
    # outras opcoes
    else:
        interface.limpa_tela()
        print('Finalizando programa...\n'
              'Integrantes do projeto: \n'
              '     Gabriel Souza Pereira\n'
              '     Gabriel Gigante\n'
              '     Priscila Barros\n'
              '     Saulo Martins\n'
              '     Itanu Romero\n')
        break
