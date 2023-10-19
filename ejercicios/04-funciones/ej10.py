"""
10-Crea una función llamada calcular_factorial que tome un número entero como
parámetro y devuelva el factorial de ese número. El factorial de un número
entero positivo n se define como el producto de todos los números enteros
positivos desde 1 hasta n.


"""


def calcular_factorial(numero):
    factorial = 1

    for i in range(1, numero + 1):
        factorial *= i

    return factorial


numero = int(input('Ingrese un numero'))


print(f'El factorial es {calcular_factorial(numero)}')



