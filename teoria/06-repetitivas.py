"""
ESTRUCTURAS REPETITIVAS, ITERATIVAS, CICLICAS

# bucle while
# bucle for

"""


# BUCLE WHILE
"""
- Se suele utilizar cuando no sabemos la cantidad de veces que queremos repetir el codigo.
- El final el bucle esta controlado por una condicion


"""

""" saldo_bancario = 100000

plazo_fijo = float(input('Ingrese el monto que quiere invertir: '))

while plazo_fijo > saldo_bancario:
    print('Saldo insuficiente.')
    plazo_fijo = float(input('Ingrese nuevamente: '))

print('Inversion constituida! :)')

"""


"""
VARIABLES ESPECIALES

CONTADORES => Sirven para contar la cantidad de veces que se ejecuta un bucle.

ACUMULADORES => Almacenan el incremento (o decremento) de una variable.

BANDERAS => Es un booleano que corta el bucle ante una determinada condicion.

"""
""" 
seguir = True


while seguir:
    respuesta = input('Queres jugar nuevamente? si/no: ')

    if respuesta == 'no':
        seguir = False
 """


# BUCLE FOR


"""
=> Recorren una secuencia de valores.
=> Se la suele utilizar cuando sabemos cuantas repetir el bucle.
=> El ciclo se va a ejecutar una vez por cada valor en la secuencia.

"""

""" alumnos = ['Diego', 'Rocio', ' Bruno', 'Hernan']

for persona in alumnos:
    print(persona)
 """


""" numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in numeros:
    print('En esta iteracion i vale: ', i)
 """

# ITERANDO UN DICCIONARIOS

""" calificaciones = {
    'Zoe' : 9,
    'Lea' : 7,
    'Tomi' : 4
}

for i in calificaciones:
    print(i)

 """


""" 

for i in range(1, 101):
    print(i) """




# BREAK => detener el bucle
# CONTINUE => salta la iteracion actual.

numeros = [1,2, 3, 4, 5, 6, 7, 8, 9, 10]


for numero in range(1,11):
    
    if numero ==4:
        continue
    print(numero)
    

print('Estoy fuera del bucle')