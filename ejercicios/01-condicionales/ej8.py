"""
-Escribir un programa que pida al usuario una cadena de caracteres y muestre por pantalla si contiene la letra "a".

"""


cadena = input('Ingrese una cadena de caracteres: ')


if 'A' in cadena.upper():
    print('Contiene la letra "A" ')
else:
    print('No contiene la letra "A"')