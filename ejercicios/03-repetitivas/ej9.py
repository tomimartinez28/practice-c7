"""
9-Escribe un programa que pida al usuario un número y luego imprima la secuencia de Fibonacci correspondiente a ese número.

"""

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89



num = int(input('Ingese un numero: '))

a, b = 0, 1


while b <= num:
    print(b)
    a, b = b, a + b
    


