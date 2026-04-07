opcion = 0
cantidad_notas = 0
total_notas_curso = 0
promedio_notas_curso = 0

while opcion != 3:
    print("=== REGISTRO FINAL DE NOTAS ===")
    print("Por favor, seleccione una opción:")
    print("1. Registrar notas")
    print("2. Mostrar analisis de notas")
    print("3. Salir")

    opcion = int(input("Ingrese su opcion (ingrese un valor númerico entero): "))

    match opcion:
        case 1:
            cantidad_notas = int(input("Introduzca la cantidad de notas a registrar: "))
            if cantidad_notas < 5:
                print("No puede registrar las notas, debe registrar al menos 5 notas.")
                continue

            contador = 0
            while contador < cantidad_notas:
                total_notas_curso += float(input("Introduzca la nota que desea registrar (Se aceptan decimales): "))
                contador += 1
        case 2:
            if cantidad_notas <= 0:
                print("No se han registrado notas, por favor registre las notas antes de mostrar el análisis.")
                continue

            promedio_notas_curso = total_notas_curso / cantidad_notas
            print(f"La cantidad de notas registradas es: {cantidad_notas}")
            print(f"El promedio de las notas del curso es: {promedio_notas_curso}")

            if promedio_notas_curso > 3.9:
                print("=== ¡CURSO APROBADO! :D ===")
            else:
                print("=== ¡CURSO REPROBADO! :c ===")

        case _:
            print("¡Muchas gracias por usar el programa! :D")
            print("Fin del registro...")
