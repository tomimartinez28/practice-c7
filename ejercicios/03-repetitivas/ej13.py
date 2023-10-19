"""
13-Escribe un programa que pida al usuario un número y luego imprima un triángulo de asteriscos con esa cantidad de filas.



*
**
***
****
*****

"""

num_filas = int(input('ingrese el numero de filas: '))


for fila in range(num_filas):
    print('*' * (fila + 1))
    
