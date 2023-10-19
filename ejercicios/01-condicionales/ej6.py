"""
6-Escribir un programa que pida al usuario un número entero y muestre por pantalla si es múltiplo de 2 y de 3 a la vez.≈

"""


numero = float(input('Ingrese un numero cualquiera: '))

if numero % 2 == 0 and numero % 3 == 0:
    print('El numero ingresado es multiplo de 2 y de 3 a la vez')
else:
    print('El numero ingresado NO ES multiplo de 2 y de 3 a la vez')