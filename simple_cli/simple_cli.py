"""
Librería Simple CLI
------------------
Módulo para gestionar interfaces de linea de comandos de forma simple.
Autor: Esteban Perafan
Versión: 1.0
"""

from enum import Enum
import os
import subprocess

__all__ = ['header', 'menu', 'clear']

def header(
        message="Encabezado", 
        border_divider="=", 
        border_divider_length=64,
        content_divider="-",
        content_divider_length=21,
        vertical_divider_spacing=0, 
        horizontal_divider_spacing=0, 
        top_border=True, 
        bottom_border=True
    ) -> None :
    """ Función para imprimir un encabezado elegante por consola """
    if top_border:
        _border(border_divider,border_divider_length)

    _vertical_spacing(vertical_divider_spacing)

    print(
        _content_border(content_divider, content_divider_length),
        _horizontal_spacing(horizontal_divider_spacing),
        message,
        _horizontal_spacing(horizontal_divider_spacing),
        _content_border(content_divider, content_divider_length)
    )
    
    _vertical_spacing(vertical_divider_spacing)
    
    if(bottom_border):
        _border(border_divider, border_divider_length)

def menu(
        message="Menú",
        options=None,
        border_divider="=", 
        border_divider_length=64, 
        content_divider=" ", 
        content_divider_length=20, 
        vertical_divider_spacing=0, 
        horizontal_divider_spacing=0, 
        accept_input=True,
        input_message="Por favor, indique su selección"
    ) -> int | None :
    
    if options is None:
        options = []

    header(message=message, border_divider=border_divider, border_divider_length=border_divider_length, content_divider=content_divider, content_divider_length=content_divider_length, vertical_divider_spacing=vertical_divider_spacing, horizontal_divider_spacing=horizontal_divider_spacing, bottom_border=False)
    
    options = [option.name if isinstance(option, Enum) else str(option).upper() for option in options]
    if "SALIR" not in options:
        options.append("SALIR")

    for index, value in enumerate(options):
        _menu_option(index + 1, str.capitalize(value.name) if isinstance(value, Enum) else str.capitalize(value))
    
    _border(border_divider, border_divider_length)

    if accept_input:
        response = None

        try:
            response = int(_request_input(input_message))
        except KeyboardInterrupt:
            _vertical_spacing(1)
            print("Finalizando el programa...")
        except ValueError as err:
            raise ValueError(f"Ha ingresado una opción no valida, por favor, indique un valor númerico como parte de su selección. {err}")

        try:
            if response is None or response > len(options):
                raise ValueError("Ha ingresado una opción no valida. La opción que ha seleccionado no se encuentra en el menú.")
        except ValueError as err:
            raise err

        return response

    return None

def clear():
    if os.name == "posix":
        os.environ.setdefault('TERM', 'xterm-256color')
    subprocess.run("clear" if os.name == "posix" else "cls", shell=True)

def _vertical_spacing(spacing):
    """ Función para imprimir saltos de linea una cantidad especificada de veces """
    for i in range(spacing):
            print("")

def _horizontal_spacing(spacing):
    """ Función para generar una cadena con una cantidad especificada de divisores """
    return "" * spacing

def _border(divider, length):
    print(divider * length)

def _content_border(divider, length):
    return divider * length

def _menu_option(index, value):
    print(f"{index}) {value}")

def _request_input(message):
    return input(f"{message}: ")

if __name__ == "__main__":
    print("Bienvenido a Simple CLI! Somos una libreria diseñada para gestionar interfaces de usuario en terminal de forma simple.\n")
    print("Ej:")
    print("")
    print("from simple_cli import show_header")
    print('show_header(message="Hola mundo!")')
    print("")
    print("Resultado:")
    header("Hola mundo!")