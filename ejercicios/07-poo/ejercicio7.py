"""
Ejercicio 7: Bebidas Online
Vamos a administrar un ecommerce de bebidas.
En un depósito se guardan las bebidas a comercializar.
Estos productos son bebidas como agua mineral y gaseosas.

De los productos nos interesa saber su identificador (cada uno tiene uno
distinto), cantidad de litros, precio y marca.

Si es agua mineral nos interesa saber también el origen (Manantial, Ciudad, etc).

Si es una gaseosa queremos saber el porcentaje que tiene de azúcar y si tiene o
no alguna promoción (si la tiene tendrá un descuento del 10% en el precio).

Las operaciones del almacén son las siguientes:

✅ Calcular precio de todas las bebidas: calcula el precio total de todos los
productos del almacén.

✅ Calcular el precio total de una marca de bebida: dada una marca, calcular el
precio total de esas bebidas.

✅ Agregar producto: agrega un producto, si el identificador esta repetido en
alguno de las bebidas, no se agregará esa bebida.

✅ Eliminar un producto: dado un ID, eliminar el producto del depósito.

✅ Mostrar información: mostramos para cada bebida toda su información.

"""




class Bebida:
    def __init__(self, id, litros, marca, precio):
        self.id = id
        self.litros = litros
        self.marca = marca
        self._precio = precio

    def obtener_precio(self):
        return self._precio
    
    def ver_info(self):
        for clave,valor in vars(self).items():
            print(f'{clave.upper()} => {valor}')





class Agua(Bebida):
    def __init__(self, id, litros, marca, precio, origen):
        super().__init__(id, litros, marca, precio)
        self.origen = origen



class Gaseosa(Bebida):
    def __init__(self, id, litros, marca, precio,  porcentaje_azucar, promocion = False):
        super().__init__(id, litros, marca, precio)
        self.porcentaje_azucar = porcentaje_azucar
        self.promocion = promocion

    def obtener_precio(self):
        if self.promocion:
            return self._precio * (1 - 0.1)
        return self._precio
    



class Almacen:
    def __init__(self):
        self.lista_bebidas = []



    def agregar_bebidas(self, bebida_nueva):

        # Aca valido que pertenezca a la clase Agua o Gaseosa. Si pasa este IF pertenece a alguna.
        if not isinstance(bebida_nueva, Agua) and not isinstance(bebida_nueva, Gaseosa):
            print('El dato ingreasado no pertence a la clase Agua ni Gaseosa.')
            return
        
        # Validar que el ID no exista ya en la lista.
        for b in self.lista_bebidas:
            if b.id == bebida_nueva.id:
                print(f'{bebida_nueva.marca} ya existe.')
                return
        
        self.lista_bebidas.append(bebida_nueva)
        

    def obtener_total(self, marca = None):
        total = 0

        if marca is None:
            for bebida in self.lista_bebidas:
                total += bebida.obtener_precio()
        else:
            for bebida in self.lista_bebidas:
                if bebida.marca == marca:
                    total += bebida.obtener_precio()
        
    def eliminar_producto(self, id):
        for b in self.lista_bebidas:
            if b.id == id:
                self.lista_bebidas.remove(b)
                return
        print('No se encontro el ID.')


    def ver_info_almacen(self):
        for bebida in self.lista_bebidas:
            bebida.ver_info()
            print('===============================')





almacen1 = Almacen()

bebida1 = Agua(1, 100, 'Villavicencio', 500, 'Manantial')
bebida2 = Gaseosa(2, 50, 'Coca Cola', 1000, 0.2, True)
bebida3 = Agua(2, 500 ,'Agua Express', 700, 'Manantial')


almacen1.agregar_bebidas(bebida1)
almacen1.agregar_bebidas(bebida2)
almacen1.agregar_bebidas(bebida3)

almacen1.ver_info_almacen()


almacen1.eliminar_producto(3)

almacen1.ver_info_almacen()