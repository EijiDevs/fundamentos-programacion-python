print("=== Sistema de acceso a sala ===")

cupos_disponibles = int(input("Por favor, ingrese la cantidad de cupos disponibles en la sala \n:"))
has_reserva = False

print("Por favor, indique si tiene una reserva para ingresar a la sala")
print("1. Sí, tengo una reserva")
print("2. No, no tengo una reserva")
has_reserva = True if (int(input("Indique una opción (1/2): ")) == 1) else False

if cupos_disponibles <= 0:
    print("Ingreso rechazado: sin cupos")
    exit()

if has_reserva:
    print("Ingreso permitido")
else:
    print("Ingreso rechazado: sin reserva")

print("Fin del proceso")