class Prenda:

    # una prenda unifica los dos diccionarios del enunciado (prendas + bodega) en un solo
    # objeto: los campos descriptivos y los operativos (precio, unidades) viven juntos

    def __init__(self, codigo: str, nombre: str, categoria: str, talla: str,
                 color: str, material: str, es_unisex: bool, precio: int, unidades: int):
        if not Prenda.validar_codigo(codigo):
            raise ValueError("El código no puede estar vacío.")
        if not Prenda.validar_nombre(nombre):
            raise ValueError("El nombre no puede estar vacío.")
        if not Prenda.validar_categoria(categoria):
            raise ValueError("La categoría no puede estar vacía.")
        if not Prenda.validar_talla(talla):
            raise ValueError("La talla no puede estar vacía.")
        if not Prenda.validar_color(color):
            raise ValueError("El color no puede estar vacío.")
        if not Prenda.validar_material(material):
            raise ValueError("El material no puede estar vacío.")
        if not Prenda.validar_precio(precio):
            raise ValueError("El precio debe ser un número entero mayor que cero.")
        if not Prenda.validar_unidades(unidades):
            raise ValueError("Las unidades deben ser un número entero mayor o igual a cero.")

        # guardo los textos sin espacios de sobra para que las busquedas exactas no fallen.
        # el codigo ademas lo dejo en mayusculas para que coincida con la clave del almacen
        self._codigo = codigo.strip().upper()
        self._nombre = nombre.strip()
        self._categoria = categoria.strip()
        self._talla = talla.strip()
        self._color = color.strip()
        self._material = material.strip()
        self._es_unisex = es_unisex
        self._precio = precio
        self._unidades = unidades

    @staticmethod
    def _texto_valido(valor: str) -> bool:
        # regla comun de los campos de texto: no vacio ni solo espacios en blanco
        return valor.strip() != ""

    @staticmethod
    def validar_codigo(codigo: str) -> bool:
        return Prenda._texto_valido(codigo)

    @staticmethod
    def validar_nombre(nombre: str) -> bool:
        return Prenda._texto_valido(nombre)

    @staticmethod
    def validar_categoria(categoria: str) -> bool:
        return Prenda._texto_valido(categoria)

    @staticmethod
    def validar_talla(talla: str) -> bool:
        return Prenda._texto_valido(talla)

    @staticmethod
    def validar_color(color: str) -> bool:
        return Prenda._texto_valido(color)

    @staticmethod
    def validar_material(material: str) -> bool:
        return Prenda._texto_valido(material)

    @staticmethod
    def validar_es_unisex(es_unisex: str) -> bool:
        # el usuario responde 's' o 'n'; cualquier otra cosa la considero invalida
        return es_unisex.strip().lower() in ("s", "n")

    @staticmethod
    def validar_precio(precio: int) -> bool:
        return precio > 0

    @staticmethod
    def validar_unidades(unidades: int) -> bool:
        return unidades >= 0

    @property
    def codigo(self) -> str:
        return self._codigo

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, nombre: str):
        if not Prenda.validar_nombre(nombre):
            raise ValueError("El nombre no puede estar vacío.")
        self._nombre = nombre.strip()

    @property
    def categoria(self) -> str:
        return self._categoria

    @categoria.setter
    def categoria(self, categoria: str):
        if not Prenda.validar_categoria(categoria):
            raise ValueError("La categoría no puede estar vacía.")
        self._categoria = categoria.strip()

    @property
    def talla(self) -> str:
        return self._talla

    @talla.setter
    def talla(self, talla: str):
        if not Prenda.validar_talla(talla):
            raise ValueError("La talla no puede estar vacía.")
        self._talla = talla.strip()

    @property
    def color(self) -> str:
        return self._color

    @color.setter
    def color(self, color: str):
        if not Prenda.validar_color(color):
            raise ValueError("El color no puede estar vacío.")
        self._color = color.strip()

    @property
    def material(self) -> str:
        return self._material

    @material.setter
    def material(self, material: str):
        if not Prenda.validar_material(material):
            raise ValueError("El material no puede estar vacío.")
        self._material = material.strip()

    @property
    def es_unisex(self) -> bool:
        return self._es_unisex

    @es_unisex.setter
    def es_unisex(self, es_unisex: bool):
        self._es_unisex = es_unisex

    @property
    def precio(self) -> int:
        return self._precio

    @precio.setter
    def precio(self, precio: int):
        if not Prenda.validar_precio(precio):
            raise ValueError("El precio debe ser un número entero mayor que cero.")
        self._precio = precio
        # print(f"[debug] precio de {self._codigo} -> {self._precio}")

    @property
    def unidades(self) -> int:
        return self._unidades

    @unidades.setter
    def unidades(self, unidades: int):
        if not Prenda.validar_unidades(unidades):
            raise ValueError("Las unidades deben ser un número entero mayor o igual a cero.")
        self._unidades = unidades
