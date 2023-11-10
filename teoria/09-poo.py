"""
CARACTERISTICAS

=> Abstraccion

=> Polimorfismo

=> Encapsulacion

=> Herencia

"""


class Persona:
    def __init__(self, nombre, apellido, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono

    def saludar(self):
        return f'Hola mi nombre {self.nombre}'

    def caminar(self):
        return 'Estoy caminando...'


class Estudiante(Persona):
    def __init__(self, nombre, apellido, telefono, calificacion):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.__calificacion = calificacion # _Estudiante__calificacion

    def mostrar_calificacion(self):
        return f'Hola mi nombre es {self.nombre}, y mi calificacion es {self.__calificacion}.'
    
    def caminar(self):
        return 'Estoy caminando y soy un estudiante...'
    
    def modificar_calificacion(self, calificacion_nueva):
        self.__calificacion = calificacion_nueva




# Dos objetos de la clase persona

persona1 = Persona('Tomas', 'Martinez', '12312312')
persona2 = Persona('Leandro', 'Alvarez', '12312523')

# Dos objetos de la clase estudiante
estudiante1 = Estudiante('Emiliano', 'Salgado', '58247834', 8)
estudiante2 = Estudiante('Fabricio', 'Cardozo', '82384290', 9)




estudiante1._Estudiante__calificacion = 'hola mundo'

print(vars(estudiante1))




 




