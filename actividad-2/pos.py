from simple_cli import header, menu, clear
from enum import Enum
import time

class POS(Enum):
    CREAR_PRODUCTO = 1
    VER_PRODUCTO = 2
    VER_PRODUCTOS = 3
    ELIMINAR_PRODUCTO = 4
    ABASTECER_STOCK_PRODUCTO = 5
    VER_STOCK_PRODUCTOS = 6
    VER_STOCK_PRODUCTO = 7
    CREAR_CLIENTE = 8
    VER_CLIENTE = 9
    VER_CLIENTES = 10
    ELIMINAR_CLIENTE = 11
    VENDER = 12

class MetodoPago(Enum):
    EFECTIVO = 1
    DEBITO = 2
    CREDITO = 3
    TRANSFERENCIA = 4


clientes = [] # Codigo, RUT, Nombre, Apellido, Correo
productos = [] # Codigo, Nombre, Descripcion, Stock, Precio
ventas = [] # Codigo, Codigo Cliente, Codigo Producto, Cantidad, Total, Metodo Pago, Fecha Pago, Hora Pago

if __name__ == "__main__":
    
    medio_pago_seleccionado = None

    header(message="Hola mundo! en POS")

    time.sleep(2)
    clear()

    try:
        medio_pago_seleccionado = MetodoPago(menu(
            message="Medio de pago",
            options=MetodoPago,
            input_message="Por favor, ingrese su medio de pago"
        ))
    except Exception as err:
        raise err


