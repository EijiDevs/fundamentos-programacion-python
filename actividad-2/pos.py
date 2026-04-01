from collections.abc import Callable
from typing import Any, TypedDict
from simple_cli import header, menu, clear
from enum import IntEnum
import time

# Definición alias de tipado para mejorar la legibilidad del código (define un contrato en tiempo de checking sin clases)
# TypedDict -> Nueva sintaxis para definir un diccionario con una estructura y tipos conocidos a partir de Py 3.8+
class Producto(TypedDict):
    codigo: str
    nombre: str
    descripcion: str
    stock: int
    precio: float

# type -> Nueva sintaxis para TypeAlias del modulo typing a partir de Py 3.12+
type MenuEjemploOption = dict[str, int | str | Callable[..., Any]]
type MenuEjemplo = dict[str, str | list[MenuEjemploOption]]

# Ejemplo de callable inyectable en el menu
def crear_producto() -> Producto :
    # Diccionario literal + ejecución secuencial de inputs para solicitar la información necesaria para crear un producto
    return {
        "codigo": input("Por favor, ingrese el codigo del producto: "),
        "nombre": input("Por favor, ingrese el nombre del producto: "),
        "descripcion": input("Por favor, ingrese la descripcion del producto: "),
        "stock": int(input("Por favor, ingrese el stock del producto: ")),
        "precio": float(input("Por favor, ingrese el precio del producto: ")),
    }

# Estructura de ejemplo para crear un menu sin necesidad de clases
ejemplo_estructura_menu: MenuEjemplo = {
    "id" : "",
    "description" : "",
    "options" : [
        {
            "id" : 0,
            "description" : "",
            "href" : crear_producto
        }
    ]
}

class MetodoPago(IntEnum):
    EFECTIVO = 1
    DEBITO = 2
    CREDITO = 3
    TRANSFERENCIA = 4

def main():
    opcion = None

    clientes = [] # Codigo, RUT, Nombre, Apellido, Correo
    productos = [] # Codigo, Nombre, Descripcion, Stock, Precio
    ventas = [] # Codigo, Codigo Cliente, Codigo Producto, Cantidad, Total, Metodo Pago, Fecha Pago, Hora Pago - Almacena vistas inmutables del diccionario de la transaccion con MappingProxyType

    metodo_pago_seleccionado = None

    header(message="¡¡Bienvenido a tú sistema CLI POS!!")

    time.sleep(2)
    clear()

    try:
        metodo_pago_seleccionado = MetodoPago(menu(
            message="Medio de pago",
            values=MetodoPago,
            input_message="Por favor, ingrese su medio de pago"
        ))
    except Exception as err:
        raise err

    print(metodo_pago_seleccionado)

if __name__ == "__main__": main()