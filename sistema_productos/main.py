from unittest import case

from sistema_productos.controller.producto_controller import ProductoController

opcion = None
controller = ProductoController()

while opcion != 0:
    print("1. Almacenar producto")
    print("2. Buscar producto")
    print("3. Eliminar producto")
    print("4. Modificar un producto")
    print("5. Listar productos")
    print("0. Salir")

    opcion = int(input("Ingrese su opcion: "))

    match opcion:
        case 1:
            controller.almacenar()
        case 2:
            controller.buscar()
        case 3:
            controller.eliminar()
        case 4:
            controller.modificar()
        case 5:
            controller.listar()
