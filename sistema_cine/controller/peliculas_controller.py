from model.pelicula import Pelicula

class PeliculasController:

    def __init__(self, peliculas: list[Pelicula]):
        self._peliculas = peliculas

    @property
    def peliculas(self) -> list[Pelicula]:
        return self._peliculas

    def agregar(self, titulo: str, duracion: str, calificacion: str) -> Pelicula:
        # aca hago el parseo de tipos (logica de aplicacion), las reglas de negocio
        # las valida la propia Pelicula al construirse
        try:
            duracion_int = int(duracion)
        except ValueError:
            raise ValueError("La duración debe ser un número entero.")

        try:
            calificacion_float = float(calificacion)
        except ValueError:
            raise ValueError("La calificación debe ser un número.")

        pelicula = Pelicula(titulo, duracion_int, calificacion_float)
        self._peliculas.append(pelicula)
        # print(f"[debug] agregada {titulo}, total={len(self._peliculas)}")
        return pelicula

    def buscar(self, titulo: str) -> int:
        # recorro y retorno la posicion exacta, o -1 si no esta. quien llama decide que hacer
        for indice, pelicula in enumerate(self._peliculas):
            if pelicula.titulo == titulo:
                return indice
        return -1

    def eliminar(self, indice: int) -> None:
        self._peliculas.pop(indice)

    def actualizar_disponibilidad(self) -> None:
        # aplico la regla a todos sin excepcion
        for pelicula in self._peliculas:
            pelicula.actualizar_disponibilidad()
