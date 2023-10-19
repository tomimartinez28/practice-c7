"""

10-Escribe un programa que pida al usuario una cadena de texto y luego imprima la misma cadena pero con todas las vocales en mayúscula.

"""

cadena = input('ingrese una cadena de texto: ')
cadena_modificada = ''


for letra in cadena:
    if letra in 'aeiouAEIOU':
        cadena_modificada += letra.upper()
    else:
        cadena_modificada += letra.lower()

print(f'La cadena modificada queda asi: {cadena_modificada}')

