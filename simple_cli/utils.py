def _vertical_spacing(spacing) -> None:
    """ Función para imprimir saltos de linea una cantidad especificada de veces """
    for i in range(spacing):
        print("")

def _horizontal_spacing(spacing) -> str:
    """ Función para generar una cadena con una cantidad especificada de divisores """
    return "" * spacing

def _border(divider, length) -> None:
    print(divider * length)

def _content_border(divider, length) -> str:
    return divider * length

def _menu_option(index, value) -> None:
    print(f"{index}) {value}")

def _request_input(message) -> str:
    return input(f"{message}: ")