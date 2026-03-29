from .components.header import header

if __name__ == "__main__":
    print("Bienvenido a Simple CLI! Somos una libreria diseñada para gestionar interfaces de usuario en terminal de forma simple.\n")
    print("Ej:")
    print("")
    print("from simple_cli import show_header")
    print('show_header(message="Hola mundo!")')
    print("")
    print("Resultado:")
    header("Hola mundo!")