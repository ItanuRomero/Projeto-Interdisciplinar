from database import *
import administrator
import visitor

print('Bem vindo ao PinaTalk!\n')

while True:
    print('\nQual tipo de usuário você é?\n')
    print('1 - Administrador')
    print('2 - Visitante')
    print('3 - SAIR')

    userType = str(input('\n'))

    options = ['1', '2', '3']

    if userType == '3':
        break

    if userType == '1':
        Administrador.initialize()
        
    if userType == '2':
        Visitor.initialize()

    if userType not in options:
        print('\nCódigo inserido não é inválido\n')
