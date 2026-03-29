from .components.header import header
from .utils import _indent
from textwrap import dedent

WELCOME_MESSAGE = dedent("""\
    Bienvenido a Simple CLI! 
    Somos una libreria diseñada para gestionar interfaces de usuario en terminal de forma simple.
""")

EXAMPLE_MESSAGE = dedent("""\
    Ejemplos:
    
    {code_example}
""")

RESULT_MESSAGE = dedent("""Resultado:""")

USE_HEADER_EXAMPLE = dedent("""\
    # Imprimir un encabezado con el mensaje "Hola mundo!"
    from simple_cli import header
    header("Hola mundo!")    
""")

def main():
    print(WELCOME_MESSAGE)
    print(EXAMPLE_MESSAGE.format(code_example=_indent(USE_HEADER_EXAMPLE)))
    print(RESULT_MESSAGE)
    header("Hola mundo!")

if __name__ == "__main__": main()