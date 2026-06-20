import os
import subprocess
from time import sleep

def clear() -> None:
    sleep(2)
    if os.name == "posix":
        os.environ.setdefault('TERM', 'xterm-256color')
    subprocess.run("clear" if os.name == "posix" else "cls", shell=True)

lista_nombres = []
lista_autores = []
lista_paginas = []
lista_copias = []

opcion = None
while opcion != 0:
    print("==== SISTEMA DE BIBLIOTECA ====")
    print("1. Agregar libro")
    print("2. Mostrar libros")
    print("3. Buscar libro")
    print("4. Prestar libro")
    print("5. Devolver libro")
    print("6. Mostrar libro más largo")
    print("7. Mostrar total de páginas disponibles")
    print("8. Mostrar promedio de páginas")
    print("0. Salir")

    try:
        opcion = int(input("Elige una opción: "))
    except ValueError:
        print("Opcion no valida. Por favor, ingrese una de las opciones que aparecen en el menú.")
        clear()
        continue

    if not 0 <= opcion <= 8:
        print("Opcion no valida. Por favor, ingrese una de las opciones que aparecen en el menú.")
        clear()
        continue

    match opcion:
        case 1:
            nombre_libro = None
            autor_libro = None
            cantidad_paginas = 0
            cantidad_copias = 0

            try:
                nombre_libro = input("Ingrese el nombre del libro: ")
            except:
                print("Por favor, ingrese un valor valido")
                clear()
                continue

            if nombre_libro is None or not nombre_libro.strip():
                print("Por favor, ingrese un nombre valido valido no vacio.")
                clear()
                continue

            try:
                autor_libro = input("Ingrese el autor del libro: ")
            except:
                print("Por favor, ingrese un valor valido")
                clear()
                continue

            if autor_libro is None or not autor_libro.strip():
                print("Por favor, ingrese un autor valido no vacio.")
                clear()
                continue

            try:
                cantidad_paginas = int(input("Ingrese la cantidad de páginas del libro: "))
            except ValueError:
                print("Por favor, ingrese un numero valido")
                clear()
                continue

            if cantidad_paginas <= 0:
                print("La cantidad de paginas no puede ser negativa ni igual a cero")
                clear()
                continue

            try:
                cantidad_copias = int(input("Ingrese la cantidad de copias del libro: "))
            except ValueError:
                print("Por favor, ingrese un numero valido")
                clear()
                continue

            if cantidad_copias <= 0:
                print("La cantidad de copias no puede ser negativa ni igual a cero")
                clear()
                continue

            lista_nombres.append(nombre_libro)
            lista_autores.append(autor_libro)
            lista_paginas.append(cantidad_paginas)
            lista_copias.append(cantidad_copias)

            print(f"Se ha agregado el libro '{nombre_libro}' a la base de datos")
            clear()
        case 2:
            if len(lista_nombres) == 0:
                print("AÚN NO HAY LIBROS REGISTRADOS...")
                clear()
                continue

            contador = 0
            for nombre in lista_nombres:
                    print(f'LIBRO: {nombre} - {lista_autores[contador]} - {lista_paginas[contador]} paginas - {lista_copias[contador]} copias')
                    contador = contador + 1

            input("PRESIONE ENTER PARA CONTINUAR...")
            clear()

        case 3:

            try:
                valor_busqueda = input("Por favor, ingrese el nombre del libro que busca: \n")
            except ValueError:
                print("Por favor, ingrese un valor valido")
                clear()
                continue

            if valor_busqueda is None or not valor_busqueda.strip():
                print("Por favor, ingrese un nombre valido no vacio.")
                clear()
                continue

            contador = 0
            encontrado = False
            for nombre in lista_nombres:
                if valor_busqueda == nombre:
                    encontrado = True
                    break
                contador = contador + 1

            if encontrado:
                print(f'LIBRO: {valor_busqueda} - {lista_autores[contador]} - {lista_paginas[contador]} paginas - {lista_copias[contador]} copias')
            else:
                print("Libro no encontrado")

            input("PRESIONE ENTER PARA CONTINUAR...")
            clear()
        case 4:
            nombre_libro = None
            cantidad_copias = 0

            try:
                nombre_libro = input("Ingrese el nombre del libro que desea llevar: ")
            except ValueError:
                print("Por favor, ingrese un valor valido")
                clear()
                continue

            if nombre_libro is None or not nombre_libro.strip():
                print("Por favor, ingrese un nombre valido no vacio.")
                clear()
                continue

            contador = 0
            encontrado = False
            for nombre in lista_nombres:
                if nombre_libro == nombre:
                    encontrado = True
                    break
                contador = contador + 1

            if not encontrado:
                print("Libro no encontrado")
                clear()
                continue

            try:
                cantidad_copias = int(input("Ingrese la cantidad de copias del libro que desea llevar: "))
            except ValueError:
                print("Por favor, ingrese un numero valido")
                clear()
                continue

            if cantidad_copias <= 0:
                print("La cantidad de copias a pedir no puede ser negativa ni igual a cero")
                clear()
                continue


            cantidad_copias_actual = lista_copias[contador]

            if cantidad_copias > cantidad_copias_actual:
                print("Lo sentimos, no hay suficientes copias disponibles.")
                clear()
                continue

            lista_copias[contador] = cantidad_copias_actual - cantidad_copias
            print(f'Has prestado {cantidad_copias} copias del libro "{nombre_libro}".')

            input("PRESIONE ENTER PARA CONTINUAR...")
            clear()
        case 5:
            nombre_libro = None
            cantidad_copias = 0

            try:
                nombre_libro = input("Ingrese el nombre del libro que desea devolver: ")
            except ValueError:
                print("Por favor, ingrese un valor valido")
                clear()
                continue

            if nombre_libro is None or not nombre_libro.strip():
                print("Por favor, ingrese un nombre valido no vacio.")
                clear()
                continue

            contador = 0
            encontrado = False
            for nombre in lista_nombres:
                if nombre_libro == nombre:
                    encontrado = True
                    break
                contador = contador + 1

            if not encontrado:
                print("El libro que intenta devolver no está registrado en nuestra base de datos.")
                clear()
                continue

            try:
                cantidad_copias = int(input("Ingrese la cantidad de copias del libro que desea devolver: "))
            except ValueError:
                print("Por favor, ingrese un numero valido")
                clear()
                continue

            if cantidad_copias <= 0:
                print("La cantidad de copias a devolver no puede ser negativa ni igual a cero")
                clear()
                continue

            lista_copias[contador] += cantidad_copias
            print(f'Has devuelto {cantidad_copias} copias del libro "{nombre_libro}".')

            input("PRESIONE ENTER PARA CONTINUAR...")
            clear()

        case 6:

            libro_mas_largo = 0
            mayor_cantidad_paginas = 0
            contador = 0

            for paginas in lista_paginas:
                if paginas > mayor_cantidad_paginas:
                    mayor_cantidad_paginas = paginas
                    libro_mas_largo = contador
                contador = contador + 1

            print(f'El libro con mayor cantidad de páginas es "{lista_nombres[libro_mas_largo]}" con {mayor_cantidad_paginas} páginas.')

            input("PRESIONE ENTER PARA CONTINUAR...")
            clear()

        case 7:
            pass
        case 8:
            pass
        case 9:
            pass