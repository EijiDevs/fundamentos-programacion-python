print("=== VENTA DE PRODUCTOS EN OFERTA ===")
print("¿El producto que desea comprar está en oferta?")
print("1) SI")
print("2) NO")
has_oferta = True if int(input("Introduzca su selección (1 o 2): ")) == 1 else False

if not has_oferta:
    print("EL PRODUCTO NO ESTÁ EN OFERTA")
    exit()

cantidad_productos_venta = int(input("Introduzca la cantidad de unidades del producto que desea llevar: "))

if cantidad_productos_venta < 5:
    print("SI ES POSIBLE REALIZAR LA COMPRA")
else:
    print("NO ES POSIBLE REALIZAR LA COMPRA")