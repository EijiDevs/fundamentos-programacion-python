from model.pelicula import Pelicula
from controller.peliculas_controller import PeliculasController

# el almacen existe desde que arranca el programa y vive durante toda la ejecucion
peliculas: list[Pelicula] = []

SEPARADOR = "*" * 44

def imprimir_menu() -> None:
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Agregar película")
    print("2. Buscar película")
    print("3. Eliminar película")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar películas")
    print("6. Salir")
    print("=====================================")

def seleccionar_opcion() -> int:
    while True:
        try:
            opcion = int(input("Elige una opción: "))
        except ValueError:
            print("Opción no válida. Por favor, ingrese un número entero.")
            continue
        except (EOFError, KeyboardInterrupt):
            # si se corta la entrada (Ctrl-D/Ctrl-C) salgo limpio como si eligiera salir, esto es un plus dado que me sobro tiempo desarrollando :D
            print()
            return 6

        if opcion < 1 or opcion > 6:
            print("Opción no válida. Por favor, ingrese una de las opciones que aparecen en el menú.")
            continue

        return opcion

def estado_pelicula(pelicula: Pelicula) -> str:
    return "DISPONIBLE" if pelicula.disponible else "NO RECOMENDADA"

def formatear_pelicula(pelicula: Pelicula) -> str:
    return (
        f"Título: {pelicula.titulo}\n"
        f"Duración: {pelicula.duracion}\n"
        f"Calificación: {pelicula.calificacion}\n"
        f"Estado: {estado_pelicula(pelicula)}"
    )

if __name__ == '__main__':
    peliculas_controller: PeliculasController = PeliculasController(peliculas)
    opcion_seleccionada = 0

    while opcion_seleccionada != 6:
        imprimir_menu()

        opcion_seleccionada = seleccionar_opcion()

        match opcion_seleccionada:
            case 1:
                titulo = input("Ingrese un título para la película: ")
                duracion = input("Ingrese la duración de la película (en minutos): ")
                calificacion = input("Ingrese la calificación de la película (0.0 - 10.0): ")

                # dejo que el controlador parsee y la Pelicula valide; si algo falla, no se registra
                try:
                    peliculas_controller.agregar(titulo, duracion, calificacion)
                except ValueError as error:
                    print(error)
                    continue

                print("Película agregada correctamente.")
            case 2:
                titulo = input("Ingrese el título de la película a buscar: ")

                indice = peliculas_controller.buscar(titulo)
                if indice != -1:
                    print(f"Película encontrada en la posición {indice}.")
                    print(formatear_pelicula(peliculas_controller.peliculas[indice]))
                else:
                    print(f"La película '{titulo}' no se encuentra registrada.")
            case 3:
                titulo = input("Ingrese el título de la película a eliminar: ")

                # reutilizo la busqueda de la opcion anterior para ubicarla
                indice = peliculas_controller.buscar(titulo)
                if indice != -1:
                    peliculas_controller.eliminar(indice)
                    print("Película eliminada correctamente.")
                else:
                    print(f"La película '{titulo}' no se encuentra registrada.")
            case 4:
                peliculas_controller.actualizar_disponibilidad()
                print("Disponibilidad actualizada correctamente.")
            case 5:
                # primero actualizo la disponibilidad y recien ahi muestro
                peliculas_controller.actualizar_disponibilidad()

                if not peliculas_controller.peliculas:
                    print("No hay películas registradas.")
                else:
                    print("=== LISTA DE PELICULAS ===")
                    print()
                    for pelicula in peliculas_controller.peliculas:
                        print(formatear_pelicula(pelicula))
                        print(SEPARADOR)
            case 6:
                print("Gracias por usar el sistema. Vuelva Pronto")
