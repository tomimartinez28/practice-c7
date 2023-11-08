"""
Crea una clase llamada Cuenta que tendrá los siguientes atributos:

titular (que
es una persona) y 

cantidad (puede tener decimales). 


El titular será obligatorio y la cantidad es opcional.



Implementa los siguientes métodos:

mostrar(): Muestra los datos de la cuenta.

ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.
retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.
"""


class Cuenta:
    def __init__(self, titular, cantidad = 0):
        self.titular = titular
        self.cantidad = cantidad

    def mostrar(self):
        print(f'Titular: {self.titular}\nCantidad: {self.cantidad}')


    def ingresar(self, deposito):
        if deposito >= 0:
            self.cantidad += deposito
        else:
            print('Ingrese un numero positivo.')


    def retirar(self, retiro):
        if retiro >= 0:
            self.cantidad -= retiro







cuenta1 = Cuenta('Matias Husty', 5000)

cuenta1.mostrar()

cuenta1.ingresar(5000)

cuenta1.mostrar()

cuenta1.retirar(25000)

cuenta1.mostrar()