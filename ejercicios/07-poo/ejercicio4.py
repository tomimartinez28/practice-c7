"""
Ejercicio 4: Tiempo

Crear una clase Tiempo, con atributos 
 =>hora, 
 =>minuto y 
 =>segundo, 

 que pueda ser instanciada indicando: los tres atributos, sólo la hora y minuto, o sólo la hora.

Crear además los métodos necesarios para modificar la hora en cualquier
momento de forma manual. 

Mantenga la integridad de los datos en todo
momento definiendo de tipo “private”. 

Crear una clase prueba_tiempo que
prueba una hora concreta y la modifique a su gusto mostrándola por pantalla.

"""


class Tiempo:
    def __init__(self, hora, minutos = 0, segundos = 0):
        self.__hora = hora
        self.__minutos = minutos
        self.__segundos = segundos

    def modificar_hora(self):
        hora_ingresada = input('Ingrese la hora: ')
        minutos_ingresados = input('Ingrese los minutos: ')
        segundos_ingresados = input('Ingrese los segundos: ')
        self.__hora = hora_ingresada # _Tiempo__hora
        self.__minutos = minutos_ingresados
        self.__segundos = segundos_ingresados

    def mostrar_hora(self):
        print(f'Hora: {self.__hora}')
        print(f'Minutos: {self.__minutos}')
        print(f'Segundos: {self.__segundos}')



reloj = Tiempo(21, 49, 15)

reloj.mostrar_hora()

reloj.modificar_hora()

reloj.mostrar_hora()
