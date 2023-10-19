# OPERADORES DE COMPARACION

"""
a > b
a >= b
a < b
a <= b
a == b
a != b


"""
# OPERADORES LOGICOS

"""
and => Devuelve True si ambas condiciones son True
a = True
b = False
x = a and b



or => Devuelve True si al menos una de las condiciones es True
a = False
b = False
x = a or b


not => Cambia el valor de verdad de la variable

a = False
b = not a




"""




# ESTRUCTURA IF SIMPLE



""" if INGRESO_MENSUAL >= 150000:
    print('Tu ingreso es suficiente para obtener el credito.')
if LIBRE_DEUDA:
    print('No tenes deudas al dia.')
"""



INGRESO_MENSUAL = 150000
LIBRE_DEUDA = True

# IF ANIDADO

if INGRESO_MENSUAL >= 150000:
    print('Tu ingreso es suficiente.')

    if LIBRE_DEUDA:
        print('No tenes deudas')
        print('Podes tener el credito.')



# USANDO OPERADORES LOGICOS
if INGRESO_MENSUAL >= 150000 and LIBRE_DEUDA:
    print('Podes tener el credito.')



# condicional alternativo (sentencia else)
if INGRESO_MENSUAL >= 150000 and LIBRE_DEUDA:
    print('Podes tener el credito.')
else:
    print('No podes tener el credito.')



if INGRESO_MENSUAL >= 150000:
    print('Tu ingreso es suficiente.')

    if LIBRE_DEUDA:
        print('No tenes deudas')
        print('Podes tener el credito.')
    else:
        print('tenes deudas.')

else:
    print('No tenes ingreso suficiente.')

# CONDICIONES MULTIPLES

INGRESO_MENSUAL = 120000

if INGRESO_MENSUAL > 300000:
    print('Podes sacar hasta 5 millones')
elif INGRESO_MENSUAL > 200000:
    print('Podes sacar hasta 4 millones')
elif INGRESO_MENSUAL > 100000:
    print('Podes sacar hasta 2 millones')
else:
    print('No tenes suficiente ningun credigo.')
