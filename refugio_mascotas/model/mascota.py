class Mascota:

    _prioridad: bool = False

    def __init__(self, identificador: str, nombre: str, edad: int, dias_refugio: int):
        self._identificador: str = identificador
        self._nombre: str = nombre
        self._edad: int = edad
        self._dias_refugio: int = dias_refugio

    @property
    def identificador(self) -> str:
        return self._identificador

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def edad(self) -> int:
        return self._edad

    @property
    def dias_refugio(self) -> int:
        return self._dias_refugio

    @property
    def prioridad(self) -> bool:
        return self._prioridad

    @identificador.setter
    def identificador(self, identificador: str):
        self._identificador = identificador

    @nombre.setter
    def nombre(self, nombre: str):
        self._nombre = nombre

    @edad.setter
    def edad(self, edad: int):
        self._edad = edad

    @dias_refugio.setter
    def dias_refugio(self, dias_refugio: int):
        self._dias_refugio = dias_refugio

    @prioridad.setter
    def prioridad(self, value: bool):
        self._prioridad = value

