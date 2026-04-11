total_litros_consumidos = 0.0
promedio_litros_consumidos = 0.0
cantidad_consumos_registrados = 0
opcion = None

while opcion != 3:
    print("=== Registro de Consumo de Agua ===")
    print("Por favor, seleccione una de las siguientes opciones del menú:")
    print("1. Registrar consumo de agua")
    print("2. Mostrar análisis del consumo de agua")
    print("3. Salir")

    opcion = int(input("Ingrese su opcion (Por favor, indique un valor númerico entero): "))

    match opcion:
        case 1:
            cantidad_consumos_por_registrar = int(input("Por favor, indique la cantidad de consumos que desea registrar \n:"))

            if cantidad_consumos_por_registrar < 3:
                print("La cantidad de consumos a registrar debe ser igual o mayor a 3. Por favor, intente nuevamente.")
                continue

            while cantidad_consumos_registrados < cantidad_consumos_por_registrar:
                print("Por favor, indique el periodo del dia, elija entre las siguientes opciones:")
                print("1. Mañana")
                print("2. Tarde")
                print("3. Noche")

                periodo_dia = int(input("Ingrese su opcion (Por favor, indique un valor númerico entero): "))

                match periodo_dia:
                    case 1:
                        periodo_dia = "Mañana"
                    case 2:
                        periodo_dia = "Tarde"
                    case 3:
                        periodo_dia = "Noche"
                    case _:
                        periodo_dia = "Mañana"

                cantidad_litros_consumidos = float(input(f"Por favor, indique la cantidad de litros consumidos durante el periodo de '{periodo_dia}' (Se aceptan decimales)\n:"))

                total_litros_consumidos += cantidad_litros_consumidos

                cantidad_consumos_registrados += 1

                print(f"Consumo #{cantidad_consumos_registrados} registrado: {cantidad_litros_consumidos} litros durante el periodo de '{periodo_dia}'")
        case 2:
            if total_litros_consumidos == 0 or cantidad_consumos_registrados == 0:
                print("No se han registrado consumos de agua aún. Por favor, registre consumos antes de mostrar el análisis.")
                continue

            promedio_litros_consumidos = total_litros_consumidos / cantidad_consumos_registrados

            print(f"Cantidad total de consumos registrados: {cantidad_consumos_registrados}")
            print(f"Cantidad total de litros consumidos registrados: {total_litros_consumidos}")
            print(f"Promedio de litros por consumo registrado: {promedio_litros_consumidos}")

            if promedio_litros_consumidos > 2:
                print("Consumo promedio alto")
            else:
                print("Consumo promedio adecuado")
        case 3:
            print("Fin del registro")
