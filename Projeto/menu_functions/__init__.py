from interface import *


def create_menu():
    create_line()
    create_title(f' BEM-VIND@ AO PINA_TALK ')
    create_line()
    create_message(f'Posso te ajudar a encontrar a informação que deseja!\nSelecione:\n')
    menu_options()
    create_line()
    opcao_usuario = input_option()
    return opcao_usuario


def menu_options():
    print(f'{insert_cores("amarelo")}1 - '
          f'{insert_cores("amarelo claro")}Primeira tag.\n'
          f'{insert_cores("amarelo")}2 - '
          f'{insert_cores("amarelo claro")}Segunda tag.\n'
          f'{insert_cores("amarelo")}3 - '
          f'{insert_cores("amarelo claro")}Terceira tag. {insert_cores("reset")}')


def input_option():
    while True:
        try:
            opcao = int(input('Envie o numero da categoria que quer navegar: '))
        except ValueError:
            print(insert_cores('vermelho'), 'ERRO. Tente novamente apenas com numeros inteiros.', insert_cores('reset'))
        except KeyboardInterrupt:
            print(insert_cores('vermelho'), 'Usuario preferiu nao informar.', insert_cores('reset'))
            return 3
        except Exception as erro:
            print(insert_cores('vermelho'), f'Tivemos um problema, segue:\n{erro}', insert_cores('reset'))
        else:
            if 0 < opcao < 4:
                return opcao
            else:
                print(insert_cores('vermelho'), 'Digite um valor valido.', insert_cores('reset'))
