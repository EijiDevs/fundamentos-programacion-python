MAX_CANTIDAD_ITERACIONES = 10

cantidad_negativos = 0
cantidad_positivos = 0

for i in range(0, MAX_CANTIDAD_ITERACIONES):
    numero_ingresado = 0
    try:
        numero_ingresado = int(input(f"Por favor, ingrese el número #{i + 1}.\n:"))
    except ValueError:
        print("Por favor ingrese un valor valido en el proximo intento.")
        exit()

    if numero_ingresado > 0:
        cantidad_positivos += 1
    elif numero_ingresado < 0:
        cantidad_negativos += 1

print(f"Total de positivos: {cantidad_positivos}")
print(f"Total negativos: {cantidad_negativos}")