"""
4-Crea una función llamada es_capicua que tome un número como parámetro y
devuelva True si es capicúa (es decir, si se lee igual de izquierda a derecha que de
derecha a izquierda) y False en caso contrario.
"""
from ej3 import invertir_cadena



def es_capicua(numero):
    return numero == numero[::-1]


numero_ingresado = input('Ingrese un numero: ')


print(es_capicua(numero_ingresado))