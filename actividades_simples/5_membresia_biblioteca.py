print("=== SISTEMA DE PRESTAMO DE LIBROS - BIBLIOTECA CENTRAL ===")
print("¿Posee usted actualmente una membresia activa en nuestra biblioteca?")
print("1) SI")
print("2) NO")
membresia_activa = True if int(input("Seleccione una opción (1 o 2): ")) == 1 else False

if not membresia_activa:
    print("LA PERSONA NO TIENE UNA MEMBRESÍA ACTIVA.")
    exit()

print("¿Cuántos libros desea llevar prestados?")
cantidad_libros = int(input("Ingrese la cantidad de libros: "))

if cantidad_libros < 4:
    print("SI ES POSIBLE REALIZAR EL PRÉSTAMO")
else:
    print("NO ES POSIBLE REALIZAR EL PRÉSTAMO")