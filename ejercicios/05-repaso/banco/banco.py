"""
Crea un programa en Python que permita a un usuario gestionar una cuenta bancaria simulada. El programa debe permitir al usuario realizar las siguientes operaciones:

1 - Consultar el Saldo
2 - Depositar dinero en la cuenta.
3 - Retirar dinero de la cuenta si hay suficiente saldo.
4 - Salir del programa.

"""

from functions import limpiar_terminal, obtener_contrasenia, obtener_saldo, mostrar_menu, depositar, retirar_dinero

# todos los usarios del sistemas, sus pwds, y sus saldos.
DATOS_USUARIOS = [ {'username' : 'tomimartinez28','password' : 'heladito123', 'saldo' : 0 },
            {'username' : 'zoe28','password' : 'heladito456', 'saldo' : 0 },
            {'username' : 'lea28','password' : 'heladito789', 'saldo' : 0 },
]

# Crear una lista de todos los nombres de usuario
lista_de_usernames = [usuario['username'] for usuario in DATOS_USUARIOS]







# ====================ACA ARRANCA EL PROGRAMA PRINCIPAL====================================================================================

while True:
    cerrar_programa = False
    # Le pido que ingrese el username
    print('Bienvenido al banco comision 7 S.A.')
    usuario_ingresado = input('Ingrese su usuario:\n>> ')

    # si no esta en la lista, lo vuelvo a pedir
    while usuario_ingresado not in lista_de_usernames:
        limpiar_terminal()
        print('Usuario inexistente, ingrese nuevamente.')
        usuario_ingresado = input('>> ')


    # ahora pido la contraseniA
    contrasenia_ingresada = input(f'Ingrese su contrasenia {usuario_ingresado}:\n>> ')
    intentos = 2


    # verifico que la ingresada sea igual a la contrasenia que tiene el usuario que ingreso.
    while contrasenia_ingresada != obtener_contrasenia(DATOS_USUARIOS, usuario_ingresado):
        limpiar_terminal()
        contrasenia_ingresada = input(f'Contraseña incorrecta. Quedan {intentos} intentos.Ingrese nuevamente:\n>> ')
        intentos -= 1
        if intentos == 0:
            cerrar_programa = True
            print('Ingreso mal su contraeña. Vuelva a intentarlo mas tarde.')
            break
    
    if cerrar_programa:
        continue

    print('==========================================')
    print(f'Bienvenido al sistema {usuario_ingresado}')
    print('==========================================')

    while True:
        

        mostrar_menu()
        opcion = int(input('>> '))

        if opcion == 1:
            limpiar_terminal()
            print('==========================================')
            print('Su saldo es:')
            print(obtener_saldo(DATOS_USUARIOS, usuario_ingresado))
            print('==========================================')
            
        elif opcion == 2:
            limpiar_terminal()
            importe = float(input('Ingrese un monto a depositar: '))
            depositar(DATOS_USUARIOS, usuario_ingresado, importe)
            print('==========================================')
            print(f'Deposito correctamente {importe} pesos. Su saldo actual es de {obtener_saldo(DATOS_USUARIOS, usuario_ingresado)}')
            print('==========================================')
            
        elif opcion == 3:
            limpiar_terminal()
            importe = float(input('Ingrese un monto a retirar: '))
            retirar_dinero(DATOS_USUARIOS, usuario_ingresado, importe)

        elif opcion == 4:
            limpiar_terminal()
            print('==========================================')
            print('Gracias por operar con nuestro banco. Vuelva pronto.')
            print('==========================================')
            break
        else: 
            limpiar_terminal()
            print('==========================================')
            print('Opcion incorrecta.')
            print('==========================================')