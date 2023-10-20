""" Ejercicio 1
Supongamos que estás construyendo una aplicación de gestión de tareas. Debes crear un programa que permita a los usuarios realizar las siguientes operaciones:

1 - Agregar una nueva tarea a la lista de tareas pendientes.
2 - Marcar una tarea como completada.
3 - Mostrar todas las tareas pendientes.
4 - Mostrar todas las tareas completadas.
5 - Salir de la aplicación.
"""

import os

tareas_pendientes = []
tareas_completadas = []

# FUNCIONES

def limpiar_terminal():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')



def mostar_menu():
    print('Que accion desea realizar. Ingrese un numero.\n1 - Agregar una nueva tarea a la lista de tareas pendientes.\n2 - Marcar una tarea como completada.\n3 - Mostrar todas las tareas pendientes.\n4 - Mostrar todas las tareas completadas.\n5 - Salir de la aplicación.')

def mostrar_tareas_pendientes():
    contador = 0

    limpiar_terminal()
    print('==================================')
    print('TAREAS PENDIENTES')
    for tarea in tareas_pendientes:
        print(f'{contador} - {tarea}')
        contador += 1
    print('==================================')


def mostrar_tareas_completadas():
    contador = 0
    limpiar_terminal()

    print('==================================')
    print('TAREAS COMPLETADAS')
    for tarea in tareas_completadas:
        print(f'{contador} - {tarea}')
        contador += 1
    print('==================================')


def agregar_tarea():
    limpiar_terminal()
    nueva_tarea = input('Ingrese una tarea nueva: ')
    tareas_pendientes.append(nueva_tarea)
    print(f'Agrego correctaente la tarea {nueva_tarea.upper()}')


def marcar_tarea_completada():
    limpiar_terminal()
    mostrar_tareas_pendientes()

    tarea_a_remover = int(input('Ingrese el numero de la tarea que completo: '))
    
    while tarea_a_remover >= len(tareas_pendientes):
        print('Numero invalido. Ingrese nuevamente.')
        tarea_a_remover = int(input('>> '))

    tareas_completadas.append(tareas_pendientes.pop(tarea_a_remover))
    


# ACA INICIA EL PROGRAMA

while True:
    mostar_menu()

    opcion = input('>> ')

    if opcion.isdigit():
        opcion = int(opcion)

    if opcion == 1:
        agregar_tarea()
    elif opcion == 2:
        marcar_tarea_completada()
    elif opcion == 3:
        mostrar_tareas_pendientes()
    elif opcion == 4:
        mostrar_tareas_completadas()
    elif opcion == 5:
        break
    else:
        print('Opcion existente.')

print('Fin del programa.')