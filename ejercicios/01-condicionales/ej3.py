"""
3-Escribir un programa que pida al usuario dos números y muestre por pantalla cuál de ellos es mayor.

"""

num1 = float(input('Ingrese un numero: '))
num2 = float(input('Ingrese otro numero: '))



if num1 > num2:
    print(f'{num1} es mayor a {num2}')
elif num2 > num1:
    print(f'{num2} es mayor a {num1}')
else:
    print('Son iguales')