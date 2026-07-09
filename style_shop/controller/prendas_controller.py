from model.prenda import Prenda

class PrendasController:

    def __init__(self, prendas: dict[str, Prenda]):
        self._prendas = prendas

    @property
    def prendas(self) -> dict[str, Prenda]:
        return self._prendas

    def _normalizar(self, codigo: str) -> str:
        # normalizo el codigo para que las busquedas no distingan mayusculas ni espacios de sobra
        return codigo.strip().upper()

    def unidades_categoria(self, categoria: str) -> None:
        # recorro todas las prendas y acumulo las unidades de las que sean de esta categoria.
        # la comparacion no distingue mayusculas de minusculas (POLERA == polera)
        categoria_buscada = categoria.strip().lower()
        total = 0
        for prenda in self._prendas.values():
            if prenda.categoria.lower() == categoria_buscada:
                total += prenda.unidades

        # print(f"[debug] categoria={categoria_buscada} total={total}")
        print(f"El total de unidades disponibles es: {total}")

    def busqueda_precio(self, p_min: int, p_max: int) -> None:
        # me quedo con las prendas dentro del rango y que tengan stock (unidades != 0),
        # ordenadas alfabeticamente por nombre y en el formato "Nombre--Codigo"
        encontradas = [
            prenda for prenda in self._prendas.values()
            if p_min <= prenda.precio <= p_max and prenda.unidades != 0
        ]
        encontradas.sort(key=lambda prenda: prenda.nombre)

        if not encontradas:
            print("No hay prendas en ese rango de precios.")
            return

        resultado = [f"{prenda.nombre}--{prenda.codigo}" for prenda in encontradas]
        print(f"Las prendas encontradas son: {resultado}")

    def actualizar_precio(self, codigo: str, nuevo_precio: int) -> bool:
        # si el codigo no esta retorno False y que el principal decida el mensaje
        clave = self._normalizar(codigo)
        if clave not in self._prendas:
            return False

        self._prendas[clave].precio = nuevo_precio
        return True

    def agregar_prenda(self, codigo: str, nombre: str, categoria: str, talla: str, color: str,
                       material: str, es_unisex: bool, precio: int, unidades: int) -> bool:
        # si el codigo ya existe no piso la prenda anterior, retorno False
        clave = self._normalizar(codigo)
        if clave in self._prendas:
            return False

        self._prendas[clave] = Prenda(codigo, nombre, categoria, talla, color,
                                      material, es_unisex, precio, unidades)
        # print(f"[debug] agregada {clave}, total={len(self._prendas)}")
        return True

    def eliminar_prenda(self, codigo: str) -> bool:
        # elimino de ambos "diccionarios" a la vez porque aca la prenda es un unico objeto.
        # uso pop (metodo del dict) en lugar de del
        clave = self._normalizar(codigo)
        if clave not in self._prendas:
            return False

        self._prendas.pop(clave)
        return True
