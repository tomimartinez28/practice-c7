"""
Ejercicio 1: Vehículo pt.1
A partir del siguiente diagrama de clases, implementá
clases y métodos para mostrar atributos.
"""

class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.cantidad_ruedas = ruedas


    def mostrar_atributos(self): 
        for clave, valor in vars(self).items():
            print(f'{clave.capitalize()} => {valor}')




class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada



coche1 = Coche('Rojo', 4, '180k/h', 2.4)
coche2 = Coche('Negro', 4, '200k/h', 2.6)

coche2.mostrar_atributos()











