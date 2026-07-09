from model.prenda import Prenda
from controller.prendas_controller import PrendasController

# el almacen (los dos diccionarios del enunciado unificados en objetos Prenda)
prendas: dict[str, Prenda] = {}

def imprimir_menu() -> None:
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Unidades por categoría")
    print("2. Búsqueda de prendas por rango de precio")
    print("3. Actualizar precio de prenda")
    print("4. Agregar prenda")
    print("5. Eliminar prenda")
    print("6. Salir")
    print("=====================================")

def seleccionar_opcion() -> int:
    try:
        opcion = int(input("Ingrese opción: "))
    except ValueError:
        print("Debe seleccionar una opción válida")
        return 0
    except (EOFError, KeyboardInterrupt):
        # si se corta la entrada (Ctrl-D/Ctrl-C) salgo limpio como si eligiera salir
        print()
        return 6

    if opcion < 1 or opcion > 6:
        print("Debe seleccionar una opción válida")
        return 0

    return opcion

if __name__ == '__main__':
    prendas_controller: PrendasController = PrendasController(prendas)
    opcion_seleccionada = 0

    # blindaje general: si la entrada se corta (Ctrl-D/Ctrl-C) en cualquier prompt interno,
    # cierro igual de limpio que con la opcion 6, sin dejar ningun traceback a la vista
    try:
        while opcion_seleccionada != 6:
            imprimir_menu()

            opcion_seleccionada = seleccionar_opcion()

            match opcion_seleccionada:
                case 1:
                    categoria = input("Ingrese categoría a consultar: ")
                    prendas_controller.unidades_categoria(categoria)
                case 2:
                    # el rango se ingresa como enteros: valido el tipo aca (logica de aplicacion).
                    # si algo no es entero vuelvo a pedir ambos valores
                    while True:
                        try:
                            precio_minimo = int(input("Ingrese precio mínimo: "))
                            precio_maximo = int(input("Ingrese precio máximo: "))
                        except ValueError:
                            print("Debe ingresar valores enteros")
                            continue

                        # precondicion de la funcion: ambos >= 0 y el minimo no supera al maximo
                        if precio_minimo < 0 or precio_maximo < 0 or precio_minimo > precio_maximo:
                            print("El precio mínimo y máximo deben ser mayores o iguales a cero, y el mínimo no puede superar al máximo")
                            continue

                        break

                    prendas_controller.busqueda_precio(precio_minimo, precio_maximo)
                case 3:
                    # repito el proceso mientras el usuario responda 's'
                    while True:
                        codigo = input("Ingrese código de la prenda: ")

                        # el nuevo precio debe ser un entero positivo; valido tipo y regla juntos
                        try:
                            nuevo_precio = int(input("Ingrese nuevo precio: "))
                            if not Prenda.validar_precio(nuevo_precio):
                                raise ValueError
                        except ValueError:
                            print("El precio debe ser un número entero mayor que cero")
                        else:
                            if prendas_controller.actualizar_precio(codigo, nuevo_precio):
                                print("Precio actualizado")
                            else:
                                print("El código no existe")

                        respuesta = input("¿Desea actualizar otro precio (s/n)?: ").strip().lower()
                        if respuesta != "s":
                            break
                case 4:
                    codigo = input("Ingrese código de la prenda: ")
                    nombre = input("Ingrese nombre: ")
                    categoria = input("Ingrese categoría: ")
                    talla = input("Ingrese talla: ")
                    color = input("Ingrese color: ")
                    material = input("Ingrese material: ")
                    unisex_texto = input("¿Es unisex? (s/n): ")
                    precio_texto = input("Ingrese precio: ")
                    unidades_texto = input("Ingrese unidades: ")

                    if not Prenda.validar_codigo(codigo):
                        print("El código no puede estar vacío")
                        continue
                    if not Prenda.validar_nombre(nombre):
                        print("El nombre no puede estar vacío")
                        continue
                    if not Prenda.validar_categoria(categoria):
                        print("La categoría no puede estar vacía")
                        continue
                    if not Prenda.validar_talla(talla):
                        print("La talla no puede estar vacía")
                        continue
                    if not Prenda.validar_color(color):
                        print("El color no puede estar vacío")
                        continue
                    if not Prenda.validar_material(material):
                        print("El material no puede estar vacío")
                        continue
                    if not Prenda.validar_es_unisex(unisex_texto):
                        print("Debe indicar 's' o 'n' para unisex")
                        continue

                    # el campo unisex ya paso su validacion: lo interpreto y lo convierto a bool
                    es_unisex = unisex_texto.strip().lower() == "s"

                    try:
                        precio = int(precio_texto)
                        if not Prenda.validar_precio(precio):
                            raise ValueError
                    except ValueError:
                        print("El precio debe ser un número entero mayor que cero")
                        continue

                    try:
                        unidades = int(unidades_texto)
                        if not Prenda.validar_unidades(unidades):
                            raise ValueError
                    except ValueError:
                        print("Las unidades deben ser un número entero mayor o igual a cero")
                        continue

                    # todos los datos validos: recien aca intento agregar (falla si el codigo ya existe)
                    if prendas_controller.agregar_prenda(codigo, nombre, categoria, talla, color,
                                                         material, es_unisex, precio, unidades):
                        print("Prenda agregada")
                    else:
                        print("El código ya existe")
                case 5:
                    codigo = input("Ingrese código de la prenda a eliminar: ")

                    if prendas_controller.eliminar_prenda(codigo):
                        print("Prenda eliminada")
                    else:
                        print("El código no existe")
                case 6:
                    print("Programa finalizado.")
    except (EOFError, KeyboardInterrupt):
        print()
        print("Programa finalizado.")
