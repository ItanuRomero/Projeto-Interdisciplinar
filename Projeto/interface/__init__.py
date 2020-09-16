def create_line(tamanho=35):
    print('-' * tamanho)


def create_title(mensagem):
    print(insert_cores("verde"), f'{mensagem:-^33}', insert_cores("reset"))


def create_message(mensagem):
    print(insert_cores("verde"), f'{mensagem}', insert_cores("reset"))


def insert_cores(cor, fundo_ou_frente=0):
    cores = {
        'preto': ['\033[1;30m', '\033[1;40m'],
        'vermelho': ['\033[1;31m', '\033[1;41m'],
        'verde': ['\033[1;32m', '\033[1;42m'],
        'amarelo': ['\033[1;33m', '\033[1;43m'],
        'azul': ['\033[1;34m', '\033[1;44m'],
        'magenta': ['\033[1;35m ', '\033[1;45m'],
        'cyan': ['\033[1;36m ', '\033[1;46m'],
        'cinza claro': ['\033[1;37m', '\033[1;47m'],
        'cinza escuro': ['\033[1;90m', '\033[1;100m'],
        'vermelho claro': ['\033[1;91m', '\033[1;101m'],
        'verde claro': ['\033[1;92m', '\033[1;102m'],
        'amarelo claro': ['\033[1;93m', '\033[1;103m'],
        'azul claro': ['\033[1;94m', '\033[1;104m'],
        'magenta claro': ['\033[1;95m', '\033[1;105m'],
        'cyan claro': ['\033[1;96m', '\033[1;106m'],
        'branco': ['\033[1;97m', '\033[1;107m'],
        'negrito': ['\033[;1m'],
        'inverte': ['\033[;7m'],
        'reset': ['\033[0;0m']
    }
    return cores[cor][fundo_ou_frente]


def limpa_tela():
    import os
    import platform
    if platform.system() == 'Linux':
        os.system('clear') or None
    else:
        os.system('cls') or None
