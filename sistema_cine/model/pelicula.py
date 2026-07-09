class Pelicula:

    # umbral a partir del cual una pelicula se considera recomendada para exhibicion
    UMBRAL_DISPONIBLE: float = 7.0

    def __init__(self, titulo: str, duracion: int, calificacion: float):
        # valido cada campo por separado antes de guardar nada,
        # asi si algo falla no me queda una pelicula a medio construir
        self._validar_titulo(titulo)
        self._validar_duracion(duracion)
        self._validar_calificacion(calificacion)

        self._titulo = titulo.strip()  # guardo el titulo sin espacios para que la busqueda exacta no falle
        self._duracion = duracion
        self._calificacion = calificacion
        self._disponible = False

    def _validar_titulo(self, titulo: str) -> None:
        if titulo.strip() == "":
            raise ValueError("El título no puede estar vacío.")

    def _validar_duracion(self, duracion: int) -> None:
        if duracion <= 0:
            raise ValueError("La duración debe ser un número entero mayor que cero.")

    def _validar_calificacion(self, calificacion: float) -> None:
        if calificacion < 0.0 or calificacion > 10.0:
            raise ValueError("La calificación debe ser un número entre 0.0 y 10.0.")

    @property
    def titulo(self) -> str:
        return self._titulo

    @titulo.setter
    def titulo(self, titulo: str):
        self._validar_titulo(titulo)
        self._titulo = titulo.strip()

    @property
    def duracion(self) -> int:
        return self._duracion

    @duracion.setter
    def duracion(self, duracion: int):
        self._validar_duracion(duracion)
        self._duracion = duracion

    @property
    def calificacion(self) -> float:
        return self._calificacion

    @calificacion.setter
    def calificacion(self, calificacion: float):
        self._validar_calificacion(calificacion)
        self._calificacion = calificacion

    @property
    def disponible(self) -> bool:
        return self._disponible

    @disponible.setter
    def disponible(self, disponible: bool):
        self._disponible = disponible

    def actualizar_disponibilidad(self) -> None:
        # regla: si la calificacion alcanza el umbral, queda recomendada
        self._disponible = self._calificacion >= self.UMBRAL_DISPONIBLE
        # print(f"[debug] {self._titulo} -> {self._calificacion} -> {self._disponible}")
