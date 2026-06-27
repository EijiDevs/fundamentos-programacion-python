from model import mascota
from refugio_mascotas.model.mascota import Mascota
from refugio_mascotas.persistence.mascotas_in_memory import MascotasInMemory

class MascotasController:
    def __init__(self):
        self.mascotas = MascotasInMemory()

    def agregar(self, identificador: str, nombre: str, edad: int, dias_refugio: int) -> None:

        if not identificador.strip():
            raise ValueError("El identificador no puede estar vacío ni contener solo espacios.")

        mascota = Mascota(
            identificador=identificador,
            nombre=nombre,
            edad=edad,
            dias_refugio=dias_refugio
        )

        self.mascotas.agregar(mascota)