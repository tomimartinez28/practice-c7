
while True:
    try:
        num1 = float(input('Introduce un numero: '))
        num2 = float(input('Introduce otro numero: '))
        print(f'La division es {num1 / num2}')
    except ZeroDivisionError:
        print('No se puede dividir por 0.')
    except ValueError:
        print('Ingrese un numero')
    finally:   
        print('Gracias por usarlo.')







print('=======================================')
print(' =======> Aca sigue el programa...')
print('=======================================')









# ZeroDivisionError

# TypeError

# ValueError

# KeyError

# IndexError