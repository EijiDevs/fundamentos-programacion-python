
opcion = None
cantidad_ventas = 0
total_ventas = 0
promedio_venta = 0
while opcion != 3:
    print("=== Registro Diario de Ventas ===")
    print("Por favor, seleccione una de las siguientes opciones del menú:")
    print("1. Registrar Ventas")
    print("2. Mostrar analisis de Ventas")
    print("3. Salir")

    opcion = int(input("Ingrese el número de la opción que desea seleccionar: "))

    match opcion:
        case 1:
            print("Opción 1 seleccionada: Registrar Ventas")
            cantidad_ventas = int(input("Por favor, ingrese la cantidad de ventas a registrar: "))
            if cantidad_ventas < 5:
                 print("La cantidad de ventas a registrar debe ser mayor a 5. Por favor, intente nuevamente.")
                 continue
            for i in range(cantidad_ventas):
                total_ventas += float(input(f"Ingrese el monto total de la venta #{i + 1} (Se aceptan decimales): "))
        case 2:
            print("Opción 2 seleccionada: Mostrar análisis de Ventas")
            if cantidad_ventas == 0:
                print("No se han registrado ventas aún. Por favor, registre ventas antes de mostrar el análisis.")
                continue

            promedio_venta = total_ventas / cantidad_ventas

            print(f"Cantidad total de ventas registradas: {cantidad_ventas}")
            print(f"Monto total de ventas registradas: {total_ventas}")
            print(f"Promedio por venta: {promedio_venta}")

            if promedio_venta > 50000:
                print("=== ¡VENTAS SOBRE EL PROMEDIO ESPERADO! ===")
            else:
                print("=== ¡VENTAS BAJO EL PROMEDIO ESPERADO! ===")

        case _:
            cantidad_ventas = 0
            total_ventas = 0
            promedio_venta = 0
            print("Gracias por utilizar el sistema de registro diario de ventas. ¡Hasta luego!")
            print("Fin del registro...")
