from .components import header, menu
from .utils import _indent
from textwrap import dedent
from enum import Enum

WELCOME_MESSAGE = dedent("""\
    Bienvenido a Simple CLI! 
    Somos una libreria diseñada para gestionar interfaces de usuario en terminal de forma simple.""")

EXAMPLE_MESSAGE = dedent("""\
    
    Ejemplo:
    
    {code_example}
""")

RESULT_MESSAGE = dedent("""Resultado:""")

USE_HEADER_EXAMPLE = dedent("""\
    # Imprimir un encabezado con el mensaje "Hola mundo!"
    from simple_cli import header
    header("Hola mundo!")    
""")

USE_MENU_EXAMPLE = dedent("""\
    # Imprimir un menu sin solicitar un entrada, haciendo uso de un Enum
    from simple_cli import menu
    
    class EnumExample(Enum):
        EXAMPLE_1 = 1
        EXAMPLE_2 = 2
        EXAMPLE_3 = 3
        EXAMPLE_4 = 4
    
    menu(
        message="Encabezado de ejemplo para menú",
        values=EnumExample,
        accept_input=False
    )
""")

def main():
    class EnumExample(Enum):
        EXAMPLE_1 = 1
        EXAMPLE_2 = 2
        EXAMPLE_3 = 3
        EXAMPLE_4 = 4

    print(WELCOME_MESSAGE)
    print(EXAMPLE_MESSAGE.format(code_example=_indent(USE_HEADER_EXAMPLE)))
    print(RESULT_MESSAGE)
    header("Hola mundo!")
    print(EXAMPLE_MESSAGE.format(code_example=_indent(USE_MENU_EXAMPLE)))
    print(RESULT_MESSAGE)
    menu(
        message="Encabezado de ejemplo para menú",
        values=EnumExample,
        accept_input=False
    )

if __name__ == "__main__": main()