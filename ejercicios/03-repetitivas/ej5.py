"""
5-Escribe un programa que imprima la suma de todos los números pares del 1 al 100.

"""

sumatoria = 0


for numero in range(0, 101, 2):
    sumatoria += numero


print(f'La suma de todos los numeros pares del 1 al 100 es: {sumatoria}')