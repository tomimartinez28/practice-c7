"""
Nos piden que diseñemos un programa para gestionar donaciones de alimentos. Los productos tienen los siguientes atributos:

=> ✅ Nombre
=>✅ Cantidad

Tenemos dos tipos de productos:

=> ✅Perecedero: tiene un atributo llamado días a caducar.

=> ✅No perecedero: tiene un atributo llamado tipo.

[ ✅GENERICO ]
Tendremos una metodo llamada Calcular, que según cada clase hará una cosa u otra,

 a esta función se le envía la cantidad por producto y entidades a las cuáles se entregarán donaciones.
Debe obtener la cantidad que se enviará a cada entidad, sabiendo que la distribución debe ser lo más equitativa posible. En caso que sobren productos, se almacenan para el próximo ciclo de donación.


[ ✅PERECEDERO ]
Además si el producto es perecedero, se informará:
Si le queda menos de 10 días para caducar, la entrega debe hacerse en el día actual.
Si le queda 1 mes para caducar, la entrega debe hacerse en el plazo de 1 semana.

[ NO PERECEDERO ]
Si fuera No Perecedero, se informa cuántos productos se entregarán por entidad y que queda libre la elección de la fecha de entrega siempre que no supere el mes.
"""


class Producto:
    def __init__(self, nombre, cantidad_total):
        self.nombre = nombre
        self.cantidad_total = cantidad_total

    def calcular(self, cantidad_a_donar, lista_instituciones):
        if cantidad_a_donar <= self.cantidad_total:
            cantidad_por_entidad = cantidad_a_donar // len(lista_instituciones)
            sobrante = cantidad_a_donar % len(lista_instituciones)
            print(f'Para cada entidad se destinara {cantidad_por_entidad} unidades.\n Sobraron {sobrante}para la proxima.')
        else:
            print('Cantidad insuficiente.')
            return
            


class Perecedero(Producto):
    def __init__(self, nombre, cantidad_total, dias_a_caducar):   
        super().__init__(nombre, cantidad_total)
        self.dias_a_caducar = dias_a_caducar

    def calcular(self, cantidad_a_donar, lista_instituciones):
        super().calcular(cantidad_a_donar, lista_instituciones)

        if self.dias_a_caducar < 10:
            print(f'Te quedan {self.dias_a_caducar} para que caduque. Tenes que donarlo hoy!')
        elif self.dias_a_caducar < 30:
            print(f'Te quedan {self.dias_a_caducar} para que caduque. Tenes una semana para donarlo.')
        else:
            print(f'Te quedan {self.dias_a_caducar} para que caduque')




class NoPerecedero(Producto):
    def __init__(self, nombre, cantidad_total, tipo):
        super().__init__(nombre, cantidad_total)
        self.tipo = tipo

    def calcular(self, cantidad_a_donar, lista_instituciones):
        super().calcular(cantidad_a_donar, lista_instituciones)
        print('Queda libre la elección de la fecha de entrega siempre que no supere el mes')
    


producto1 = Perecedero('Leche', 20, 25)
producto2 = NoPerecedero('Arroz', 10, 'Granos')


lista_instituciones = ['Comedor 123', 'Merendero', 'Hogar de Niñas', 'Otra institucion']


producto2.calcular(6, lista_instituciones)