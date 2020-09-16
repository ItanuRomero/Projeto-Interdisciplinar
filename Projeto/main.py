import menu_functions as menu
import interface
# import database
interface.limpa_tela()
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
              '     Gabriel Gigante\n'
              '     Gabriel Souza Pereira\n'
              '     Itanu Romero\n'
              '     Saulo Martins\n'
              '     Priscila Barros')
        break
