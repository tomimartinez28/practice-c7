""" 
Diferencia entre parametro y argumento
=> Parametro: Es la variable que se define cuando se declara la funcion
=> Argumento: El valor el real que se le pasa a la funcion cuando se la llama.
 """




def calcular_iva(monto):
    '''
    Calcula el IVA a tasa general.

    Parametros:
    - Monto imponible.

    Retorna:
    - El import del impuesto
    
    '''
    return monto * 0.21


importe = int(input('Ingresa un monto: '))
print(calcular_iva(importe))




lista_frutas = ['banana', 'manzana', 'naranjas']



# mi propio len

def len_de_tomi(lista):
    contador = 0
    for elemento in lista:
        contador += 1
    return contador



print(len_de_tomi(lista_frutas))






# Parametros por posicion => 

def monto_a_pagar(monto, porcentaje_descuento):
    descuento = monto * porcentaje_descuento
    return monto - descuento


print('El monto a pagar es:', monto_a_pagar(1000000, 0.1))


# paso de parametros por nombre

def calificar(nombre='Fulanito', calificacion='SinCalificacion'):
    print(f'Hola {nombre}, tu calificacion fue {calificacion}')


calificar()






# ARGUMENTOS INDETERMINADOS POSICIONALES 
# se los define con *nombre, se agrupan como una tupla dentro de la funcion

def saludar(*args):
    for alumno in args:
        print(f'Hola {alumno}')


saludar('Zoe', 'Leandro','Mariano')

# ARGUMENTOS INDETERMINADOS DE PALABRAS CLAVES
# se los define con **nombre y se agrupan en forma de diccionario

def calificaciones(**kwargs):
    for alumno in kwargs:
        print(f'{alumno} saco {kwargs[alumno]}')


calificaciones(zoe=10, tomi=4)
