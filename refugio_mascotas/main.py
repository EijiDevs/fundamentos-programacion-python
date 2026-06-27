from refugio_mascotas.controller.mascotas_controller import MascotasController

def imprimir_menu() -> None:
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Registrar mascota")
    print("2. Buscar mascota")
    print("3. Eliminar mascota")
    print("4. Actualizar prioridades")
    print("5. Mostrar mascotas")
    print("6. Salir")
    print("====================================")

def seleccionar_opcion() -> int | None:
    while True:
        try:
            opcion = int(input("Elige una opción: "))
        except ValueError:
            print("Opcion no valida. Por favor, ingrese un número entero.")
            continue

        if opcion < 1 or opcion > 6:
            print("Opcion no valida. Por favor, ingrese una de las opciones que aparecen en el menú.")
            continue

        return opcion

if __name__ == '__main__':
    mascotas_controller = MascotasController()
    opcion_seleccionada = None

    while opcion_seleccionada != 6:
        imprimir_menu()

        opcion_seleccionada = seleccionar_opcion()

        if opcion_seleccionada is None:
            print("Opción no válida. Por favor, ingrese un número entero entre 1 y 6.")
            continue

        match opcion_seleccionada:
            case 1:
                print("========== 1) Registrar mascota ==========")

                identificador_mascota = input("Ingrese un identificador para la mascota: ")
                nombre_mascota = input("Ingrese un nombre para la mascota: ")

                try:
                    edad_mascota = int(input("Ingrese una edad para la mascota: "))
                except ValueError:
                    print("Edad no válida. Por favor, ingrese un número entero.")
                    continue

                try:
                    dias_refugio_mascota = int(input("Ingrese la cantidad de dias que lleva en el refugio la mascota: "))
                except ValueError:
                    print("Días en refugio no válidos. Por favor, ingrese un número entero.")
                    continue

                try:
                    mascotas_controller.agregar(
                        identificador_mascota,
                        nombre_mascota,
                        edad_mascota,
                        dias_refugio_mascota
                    )
                except ValueError as e:
                    print(f"{e}")
                    continue



