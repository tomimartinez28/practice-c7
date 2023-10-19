"""

3-Escribe un programa que pida al usuario un número y luego imprima la tabla de multiplicar correspondiente a ese número del 1 al 10.
"""

numero = int(input('Ingrese un numero: '))

# con bucle for
""" for i in range(1, 11):
    resultado = i * numero
    print(f'{numero} x {i} es igual a {resultado}') """


#con bucle while

i = 1

while i <= 10:
    print(f'{numero} x {i} es {numero * i}')
    i += 1


print('Programa terminado')