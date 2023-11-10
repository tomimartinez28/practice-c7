"""
Vamos a crear un programa para nuestros libros favoritos.

Queremos mantener una lista de los libros que hemos ido leyendo, calificando según nos haya gustado más o menos al leerlo.
Para ello, crear la clase Libro, cuyos atributos son el titulo, el autor, el número de páginas y la calificación que le damos entre 0 y 10.

Crear los métodos para poder modificar y obtener los atributos si tienen sentido.


✅ Posteriormente, crear una clase ConjuntoLibros, que almacena un conjunto de libros. 

✅ Se pueden añadir libros que no existan (siempre que haya espacio), 


✅ eliminar libros por título o autor, 

✅ mostrar por pantalla los libros con la mayor y menor calificación dada y,
✅  por último, mostrar un contenido de todo el conjunto.


"""

class Libro:
    def __init__(self, titulo, autor, paginas, calificacion):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.calificacion = calificacion
    

    def __str__(self):
        return self.titulo

    # modificar atributos
    def modificar_titulo(self, titulo_nuevo):
        self.titulo = titulo_nuevo

    def modificar_autor(self, autor_nuevo):
        self.autor = autor_nuevo

    def modificar_paginas(self, paginas_nuevas):
        self.paginas = paginas_nuevas
        
    def modificar_calificacion(self, calificacion_nueva):
        self.calificacion = calificacion_nueva

    # retornar a los atributos
    def obtener_titulo(self):
        return self.titulo
    
    def obtener_autor(self):
        return self.autor
    
    def obtener_paginas(self):
        return self.paginas
    
    def obtener_calificacion(self):
        return self.calificacion
    


class ConjuntoLibros:
    def __init__(self,nombre, capacidad):
        self.nombre = nombre
        self.capacidad = capacidad
        self.lista_libros = []


    def agregar_libro(self, libro):
        if isinstance(libro, Libro):
            if libro in self.lista_libros:
                print('El libro ya existe.')
                return

            if self.capacidad > len(self.lista_libros):
                self.lista_libros.append(libro)
                print(f'El libro {libro.obtener_titulo()} fue agregado correctamente.')
            else:
                print('La capacidad esta al limite :(')
        else:
            print('No pertenece a la clase Libro.')


    def eliminar_libro_titulo(self, titulo):
        for libro in self.lista_libros:
            if libro.obtener_titulo().lower() == titulo.lower():
                self.lista_libros.remove(libro)
                print(f'Se elimino {titulo}')


    def eliminar_libro_autor(self, autor):

        libros_eliminados = []

        for libro in self.lista_libros:
            if libro.obtener_autor().lower() == autor.lower():
                self.lista_libros.remove(libro)
                libros_eliminados.append(libro)

        print(f'Se eliminaron los siguientes libros del autor {autor}')
        for libro in libros_eliminados:
            print(f'=> {libro.obtener_titulo()}')



    def mayor_calificacion(self):
        lista_de_calificaciones = [libro.obtener_calificacion() for libro in self.lista_libros]

        maxima_calificacion = max(lista_de_calificaciones)

        libros_maxima_calificacion = [libro for libro in self.lista_libros if libro.obtener_calificacion() == maxima_calificacion]

        print('Los libros con maxima calificacion son:')
        for libro in libros_maxima_calificacion:
            print('==========================================')
            print(f'{libro} - Calificacion: {libro.obtener_calificacion()}')





    def menor_calificacion(self):
        lista_de_calificaciones = [libro.obtener_calificacion() for libro in self.lista_libros]
        minima_calificacion = min(lista_de_calificaciones)
        libros_minima_calificacion = [libro for libro in self.lista_libros if libro.obtener_calificacion() == minima_calificacion]

        print('Los libros con minima calificacion son:')
        for libro in libros_minima_calificacion:
            print('==========================================')
            print(f'{libro} - Calificacion: {libro.obtener_calificacion()}')


    def mostar_libros(self):
        print('==========================================')
        
        for libro in self.lista_libros:
            print(f'{libro.obtener_titulo()} - Autor: {libro.obtener_autor()} - Calificacion: {libro.obtener_calificacion()}')





# Instancio la clase ConjuntoLibro
biblioteca = ConjuntoLibros('Favoritos', 20)


# Instancio libros
the_alchemist = Libro('The Alchemist', 'Paulo Coelho', 200, 8.8)
libro2 = Libro('1984', 'George Orwell', 300, 9.4)
libro3 = Libro('The Lord of The Rings', 'J.r.r. Talkien', 1200, 10)
libro4 = Libro('Orgullo y Prejuicio', 'Jane Austen', 400, 9.2)
libro5 = Libro('The Da Vinci Code', 'Dan Brown', 200, 10)


# Agrego los libros a la biblioteca
biblioteca.agregar_libro(the_alchemist)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)
biblioteca.agregar_libro(libro4)
biblioteca.agregar_libro(libro5)


biblioteca.mayor_calificacion()



