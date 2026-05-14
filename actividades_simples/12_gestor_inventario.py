from typing import TypedDict

class Producto(TypedDict):
    id: int
    nombre: str
    precio: float
    cantidad: int
    categoria: str

inventario : list[Producto] = [
    Producto(
        id = 1,
        nombre = "CAFÉ EN GRANO PREMIUM (1KG)",
        precio = 18990,
        cantidad = 10,
        categoria = "ALIMENTOS",
    ),
    Producto(
        id = 2,
        nombre = "CAFÉ MOLIDO NESCAFE (250G)",
        precio = 3290,
        cantidad = 20,
        categoria = "ALIMENTOS",
    ),
    Producto(
        id = 3,
        nombre = "LECHE DESCREMADA SIN LACTOSA 1L",
        precio = 1230,
        cantidad = 30,
        categoria = "ALIMENTOS",
    )
]

opcion_seleccionada = None
while opcion_seleccionada != 0:
    print("==== MENÚ PRINCIPAL ====")
    print("1. Agregar producto")
    print("2. Listar inventario")
    print("3. Buscar producto")
    print("4. Actualizar stock")
    print("5. Eliminar producto")
    print("6. Reporte stock bajo")
    print("0. Salir")
    opcion_seleccionada = int(input("Elige una opción: "))

    if not opcion_seleccionada >= 0 and opcion_seleccionada <= 6:
        print("Opcion no valida. Por favor, ingrese una de las opciones que aparecen en el menú.")
        continue

    match opcion_seleccionada:
        case 1:
            pass
            print("==== AGREGAR PRODUCTO ====")
            nombre = input("Nombre: ")
            precio = int(input("Precio: "))
            cantidad = int(input("Cantidad: "))
            categoria = input("Categoria: ")

            # Validaciones de entrada

            # Encontrar el siguiente id (id max + 1)
            id = inventario[-1]["id"] + 1

            # Agregar producto a la lista
            inventario.append(Producto(
                id = id,
                nombre = nombre,
                precio = precio,
                cantidad = cantidad,
                categoria = categoria,
            ))
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass
        case 5:
            pass
        case 6:
            pass
        case _:
            pass

    print(inventario)