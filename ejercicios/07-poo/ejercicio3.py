"""
Ejercicio 3: Triángulo
Desarrollar un programa que cargue los datos de un triángulo.
Implementar una clase con los métodos para inicializar los atributos
 imprimir el valor del lado con un tamaño mayor y 

 el tipo de triángulo que es (equilátero,
isósceles o escaleno).
"""


class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2 
        self.lado3 = lado3


    def lado_mayor(self):
        return max(self.lado1, self.lado2, self.lado3)


    def determinar_tipo(self):
        if self.lado1 == self.lado2 == self.lado3:
            return 'equilatero'
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
            return 'isósceles'
        else:
            return 'escaleno'




triagulo1 = Triangulo(8, 8, 8)

print(f'El lado mayor tiene => {triagulo1.lado_mayor()} centimetros')

print(f'Tipo de triangulo => {triagulo1.determinar_tipo()}')





