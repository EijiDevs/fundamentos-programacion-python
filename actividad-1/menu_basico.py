opcion = 0

nombre_usuario = None
edad_usuario = None
while(opcion != 4):
    print("MENÚ DE OPCIONES BÁSICO")
    print("1.- SOLICITAR NOMRE")
    print("2.- SOLICITAR EDAD")
    print("3.- MOSTRAR RESUMEN")
    print("4.- SALIR")

    opcion = input("POR FAVOR, INGRESE UNA OPCIÓN:\n")
    
    try: 
        opcion = int(opcion)
        if(opcion < 0 or opcion > 4): raise ValueError(f"LA OPCIÓN {opcion} NO ESTÁ EN EL MENÚ.")
    except ValueError as err:
        opcion = 4
        print(f"EL VALOR INGRESADO NO ES UNA OPCIÓN VALIDA. {err}")
        print("CERRANDO MENÚ...")
        exit()

    match opcion:
        case 1:
            nombre_usuario = input("POR FAVOR, INGRESE SU NOMBRE:\n")
        case 2:
            edad_usuario = int(input("POR FAVOR, INGRESE SU EDAD:\n"))
        case 3:
            print("=" * 12, "RESÚMEN", "=" * 12)
            print(f"Nombre: {nombre_usuario}")
            print(f"Edad:{edad_usuario}")
            print("=" * 33)
        case _:
            print("SALIENDO DEL PROGRAMA...")
