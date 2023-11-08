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




class Bicileta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo




class Camioneta(Coche):
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.carga = carga



class Motocicleta(Bicileta):
    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        super().__init__(color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
        


gol = Coche('Rojo', 4, '160k/h', 1.6)

amarok = Camioneta('Gris', 4, '150k/h', 2.8, '500kg')

mountain = Bicileta('Negra', 2, 'Mountain Bike')

ducati = Motocicleta('Blanca', 2, 'Deportiva', '200k/h', 2.8)

hilux = Camioneta('Violeta', 4, '150k/h', 2.8, '500kg')

lista_vehiculos = [gol, amarok, mountain, ducati, hilux]


def catalogar(lista_vehiculos):
    for vehiculo in lista_vehiculos:
        print('========================================')
        print(vehiculo)
        vehiculo.mostrar_atributos()
        print('========================================')




catalogar(lista_vehiculos)