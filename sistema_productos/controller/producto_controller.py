from sistema_productos.model.Producto import Producto

class ProductoController:

    def __init__(self):
        self.productos = []

    def almacenar(self):
        producto = Producto()

        producto.codigo = input("Ingrese el código del producto: ")
        producto.nombre = input("Ingrese el nombre del producto: ")
        producto.precio = int(input("Ingrese el precio del producto: "))
        producto.stock = int(input("Ingrese el stock del producto: "))

        disponible = input("DISPONIBLE? (SI/NO): ")
        if disponible == "SI":
            producto.disponible = True
        else:
            producto.disponible = False

        self.productos.append(producto)

    def listar(self):
        print(f"LISTA DE PRODUCTOS")

        if len(self.productos) == 0:
            print("No hay productos almacenados.")
            return

        for index, producto in enumerate(self.productos):
            print("-----------------------------")
            print(f"Producto {index + 1} de {len(self.productos)}")
            print(f"Codigo: {producto.codigo}")
            print(f"Nombre: {producto.nombre}")
            print(f"Precio: {producto.precio}")
            print(f"Stock: {producto.stock}")
            print(f"Disponible: {"SI" if producto.disponible else "NO"}")
            print(f"-----------------------------\n")

    def buscar(self):
        codigo = input("Ingrese el código del producto a buscar: ")
        encontrado = False

        for producto in self.productos:
            if producto.codigo == codigo:
                print("Producto encontrado:")
                print(f"Codigo: {producto.codigo}")
                print(f"Nombre: {producto.nombre}")
                print(f"Precio: {producto.precio}")
                print(f"Stock: {producto.stock}")
                print(f"Disponible: {"SI" if producto.disponible else "NO"}")
                encontrado = True

        if not encontrado:
            print("No se encontró el producto.")

    def eliminar(self):
        codigo = input("Ingrese el código del producto a eliminar: ")
        encontrado = False

        for index, producto in enumerate(self.productos):
            if producto.codigo == codigo:
                self.productos.pop(index)
                encontrado = True

                print("Producto eliminado exitosamente.")
                return

        if not encontrado:
            print("No se encontró el producto a eliminar.")

    def modificar(self):
        codigo = input("Ingrese el código del producto a modificar: ")
        encontrado = False

        for index, producto in enumerate(self.productos):
            if producto.codigo == codigo:
                print("Producto encontrado. Ingrese los nuevos datos:")
                producto.nombre = input("Ingrese el nuevo nombre del producto: ")
                producto.precio = int(input("Ingrese el nuevo precio del producto: "))
                producto.stock = int(input("Ingrese el nuevo stock del producto: "))

                disponible = input("DISPONIBLE? (SI/NO): ")
                if disponible == "SI":
                    producto.disponible = True
                else:
                    producto.disponible = False

                self.productos[index] = producto
                encontrado = True

                print("Producto modificado exitosamente.")
                return

        if not encontrado:
            print("No se encontró el producto a modificar.")