import os
def limpiar_terminal():
    if os.name == 'posix':
        os.system('clear')
    else: 
        os.system('cls')


def obtener_contrasenia(DATOS_USUARIOS, usuario_ingresado):
    for usuario in DATOS_USUARIOS:
        if usuario_ingresado == usuario['username']:
            return usuario['password']


def obtener_saldo(DATOS_USUARIOS, usuario_ingresado):
    for usuario in DATOS_USUARIOS:
        if usuario_ingresado == usuario['username']:
            return usuario['saldo']
        

def depositar(DATOS_USUARIOS, usuario_ingresado, saldo_a_depositar):
    for usuario in DATOS_USUARIOS:
        if usuario_ingresado == usuario['username']:
            usuario['saldo'] += saldo_a_depositar


def retirar_dinero(DATOS_USUARIOS, usuario_ingresado, importe_a_retirar):
    for usuario in DATOS_USUARIOS:
        if usuario_ingresado == usuario['username']:
            if usuario['saldo'] >= importe_a_retirar:
                usuario['saldo'] -= importe_a_retirar
            else:
                print('SALDO INSUFICIENTE.')

def mostrar_menu():
    print('Que operacion desea realizar?\n1 - Consultar el Saldo\n2 - Depositar dinero en la cuenta.\n3 - Retirar dinero de la cuenta si hay suficiente saldo.\n4 - Salir del programa.')
