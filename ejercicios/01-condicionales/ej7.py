"""

7-Escribir un programa que pida al usuario un carácter y muestre por pantalla si es una letra mayúscula, una letra minúscula, un número o un carácter especial.

"""

caracter = input('Ingrese un solo caracter: ')


if caracter.isupper():
    print('El caracter es mayuscula')
elif caracter.islower():
    print('El caracter es minuscula')
elif caracter.isdigit():
    print('El caracter es un digito')
else:
    print('El caracter es un caracter especial')