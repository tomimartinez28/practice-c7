"""
Crea un programa en Python que permita a un usuario gestionar una cuenta bancaria simulada. 

✅ El programa simular un inicio de sesión, donde se tendra un limite de tres intentos si se escribe mal la contraseña.

✅ Una vez iniciada sesion, debe permitirle al usuario:
1 - Consultar el Saldo
2 - Depositar dinero en la cuenta.
3 - Retirar dinero de la cuenta si hay suficiente saldo.
4 - Salir del programa.

"""

from functions import limpiar_terminal, obtener_contrasenia, mostrar_menu, obtener_saldo, depositar

DATOS_USUARIOS = [ {'username' : 'tomimartinez28', 'password' : 'heladito123', 'saldo' : 0},
                    {'username' : 'zoe28', 'password' : 'heladito456', 'saldo' : 0},
                    {'username' : 'lea28', 'password' : 'heladito789', 'saldo' : 0},
                ]

lista_de_usernames = [usuario['username'] for usuario in DATOS_USUARIOS]



# =========== ARRANCA EL PROGRAMA PRINCIPAL

while True:
    cerrar_programa = False
    print('Bienvenido al banco Comision 7.')

    # le pido su username
    usuario_ingresado = input('Ingrese su usuario:\n>> ')

    while usuario_ingresado not in lista_de_usernames:
        limpiar_terminal()
        print('Usuario inexistente, ingrese nuevamente.')
        usuario_ingresado = input('>> ')

    

    # le pido la password
    contrasenia_ingresada = input(f'Ingrese su contraseña {usuario_ingresado}:\n>> ')

    intentos = 2



    # valido la contrasenia
    while contrasenia_ingresada != obtener_contrasenia(DATOS_USUARIOS, usuario_ingresado):
        limpiar_terminal()

        contrasenia_ingresada = input(f'Contrasenia erronea, le quedan {intentos}intentos. Ingrese nuevamente:\f>> ')

        intentos -= 1

        if intentos == 0:
            cerrar_programa = True
            print('Ingreso mas de tres veces.')
            break
    
    if cerrar_programa:
        continue

    print('================================')
    print(f'Bienvenido al sistema {usuario_ingresado}')
    print('================================')



    # AHORA ARRANCA EL PROGRAMA BANCO
    while True:
        mostrar_menu()
        opcion = int(input('>> '))


        if opcion == 1:
            limpiar_terminal()
            print('================================')
            print(f'Su saldo es: ${obtener_saldo(DATOS_USUARIOS, usuario_ingresado)}')
            print('================================')
        elif opcion == 2:
            limpiar_terminal()
            monto = float(input('Ingrese el monto a depositar: '))
            depositar(DATOS_USUARIOS, usuario_ingresado, monto)
            print('================================')
            print(f'Deposito {monto} correctamente. Su saldo ahora es de {obtener_saldo(DATOS_USUARIOS, usuario_ingresado)}')
        elif opcion == 3:
            pass # aca terminar el ejercicio.

        elif opcion == 4:
            limpiar_terminal()
            print('Gracias por todo.')
            break


        










