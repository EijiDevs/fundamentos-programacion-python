from simple_cli import show_header, show_menu
from enum import Enum

class MetodoPago(Enum):
    EFECTIVO = 1
    DEBITO = 2
    CREDITO = 3
    TRANSFERENCIA = 4

if __name__ == "__main__":
    
    medio_pago_seleccionado = None

    show_header(message="Hola mundo! en POS")

    try:
        medio_pago_seleccionado = MetodoPago(show_menu(
            message="Medio de pago",
            options=MetodoPago,
            accept_input=True, 
            input_message="Por favor, ingrese su medio de pago"
        ))
    except:
        pass

    print(medio_pago_seleccionado)


