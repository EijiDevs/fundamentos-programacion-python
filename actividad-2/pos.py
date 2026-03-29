from simple_cli import header, menu, clear
from enum import IntEnum
import time

class POSAccionesPrincipales(IntEnum):
    VENDER = 1,
    VER_CLIENTES = 2,
    VER_PRODUCTOS = 3

class POSAccionesClientes(IntEnum):
    VER_CLIENTES = 1,
    VER_CLIENTE = 2,
    CREAR_CLIENTE = 3,
    ELIMINAR_CLIENTE = 4

class POSAccionesProductos(IntEnum):
    VER_PRODUCTOS = 1,
    VER_PRODUCTO = 2,
    CREAR_PRODUCTO = 3,
    ELIMINAR_PRODUCTO = 4,
    ABASTECER_PRODUCTO = 5

class POSAccionesVenta(IntEnum):
    SELECCIONAR_CLIENTE = 1,
    SELECCIONAR_PRODUCTO = 2,
    PAGAR = 3


class POSMetodosPago(IntEnum):
    EFECTIVO = 1
    DEBITO = 2
    CREDITO = 3
    TRANSFERENCIA = 4

def pos():
    opcion = None

    clientes = [] # Codigo, RUT, Nombre, Apellido, Correo
    productos = [] # Codigo, Nombre, Descripcion, Stock, Precio
    ventas = [] # Codigo, Codigo Cliente, Codigo Producto, Cantidad, Total, Metodo Pago, Fecha Pago, Hora Pago - Almacena vistas inmutables del diccionario de la transaccion con MappingProxyType

    metodo_pago_seleccionado = None

    header(message="¡¡Bienvenido a tú sistema CLI POS!!")

    time.sleep(2)
    clear()

    try:
        metodo_pago_seleccionado = POSMetodosPago(menu(
            message="Medio de pago",
            options=POSMetodosPago,
            input_message="Por favor, ingrese su medio de pago"
        ))
    except Exception as err:
        raise err

    print(metodo_pago_seleccionado)

if __name__ == "__main__":
    pos()