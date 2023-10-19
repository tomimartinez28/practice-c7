"""
Escribe un programa que solicite al usuario su fecha de nacimiento en formato dd/mm/aaaa y luego imprima su edad en años.
Utiliza el metodo .split()
"""

fecha_nacimiento = input('Ingresa la fecha de nacimiento en formato dd/mm/aaaa: ')
dia_nacimiento, mes_nacimiento, anio_nacimiento = fecha_nacimiento.split('/')

fecha_actual = input('Ingrese la fecha actual: ')
dia_actual, mes_actual, anio_actual = fecha_actual.split('/')


edad = int(anio_actual) - int(anio_nacimiento)

if mes_actual < mes_nacimiento or (mes_actual == mes_nacimiento and dia_actual < dia_nacimiento):
    edad -= 1


print(f'Tu edad de nacimiento es: {edad}')