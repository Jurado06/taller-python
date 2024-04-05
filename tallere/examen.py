class Producto:
    def __init__(self, nombre, precio_unitario, ubicacion, descripcion, casa, referencia, pais, unidades_compradas, garantia):
        self.id = self.generar_id()
        self.nombre = nombre
        self.precio_unitario = precio_unitario
        self.ubicacion = ubicacion
        self.descripcion = descripcion
        self.casa = casa
        self.referencia = referencia
        self.pais = pais
        self.unidades_compradas = unidades_compradas
        self.garantia = garantia

    def generar_id(self):
        # Generar id de 1 a 100 sin repetir
        pass

class Inventario:
    def __init__(self):
        self.productos = []

    def registrar_producto(self, producto):
        self.productos.append(producto)

    def buscar_productos_bodega(self):
        # Buscar y mostrar en consola todos los productos en bodega
        pass

    def buscar_producto_especifico(self, nombre):
        # Buscar y mostrar en consola (el id, el nombre, el precio unitario y la descripción) de un producto especifico este debe buscarse por nombre
        pass

    def modificar_unidades_compradas(self, nombre, unidades_nuevas):
        # Buscar y modificar el numero de unidades compradas del producto, esta modificación nunca podrá ser mayor al número inicial ingresado
        pass

    def eliminar_producto(self, nombre):
        # Eliminar un producto del inventario buscándolo por nombre, debe pedir confirmación antes de borrarlo
        pass

class Fruta:
    def __init__(self, id, nombre, precio_unitario, cantidad):
        self.id = id
        self.nombre = nombre
        self.precio_unitario = precio_unitario
        self.cantidad = cantidad

class Salpicon:
    def __init__(self):
        self.frutas = []

    def agregar_fruta(self, fruta):
        self.frutas.append(fruta)

    def costo_total(self):
        # Mostrar el costo total de un salpicón
        pass

    def frutas_ordenadas(self):
        # Mostrar todas las frutas que se digitaron ordenadas de mayor a menor costo
        pass

    def fruta_mas_barata(self):
        # Mostrar cual es la fruta más barata
        pass