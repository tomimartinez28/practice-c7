"""
2-Escribir un programa que pida al usuario un número entero y muestre por pantalla si es positivo, negativo o cero.
"""

numero = int(input('Ingresa un numero entero: '))


if numero > 0:
    print('El numero es positivo')
elif numero < 0:
    print('El numero es negativo')
else:
    print('El numero es cero')