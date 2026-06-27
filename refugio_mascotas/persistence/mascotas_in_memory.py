from refugio_mascotas.model.mascota import Mascota

class MascotasInMemory():
    def __init__(self):
        self.mascotas = []

    def agregar(self, mascota: Mascota) -> None:
        self.mascotas.append(mascota)

    def eliminar(self, nombre: str) -> None:
        pass

    def buscar_indice(self, nombre: str) -> int:
        pass

    def buscar(self, nombre: str) -> Mascota:
        pass

    def recuperar(self, nombre: str) -> Mascota:
        pass

    def listar(self) -> None:
        for mascota in self.mascotas:
            print(mascota.nombre)