from random import randint

CANTIDAD_MAXIMA_INTENTOS = 3

borde_izquierdo = 0
borde_derecho = 0
numero_aleatorio = 0

valor_intentado_usuario = 0
valor_intento_previo = 0

distancia_intento_previo = 0
distancia_intento_actual = 0

veces_intentadas = 0

print("=" * 40)
print("=" * 8 + " " + "JUEGO DENTRO DEL RANGO" + " " + "=" * 8)
print("=" * 40)

print("A continuación, por favor ingrese dos valores númericos que conformen un rango númerico valido.")
print("NOTA: El primer valor debe ser OBLIGATORIAMENTE mayor al segundo valor.")
borde_izquierdo = int(input("Por favor, ingrese el primer valor del rango (limite inferior): \n"))
borde_derecho = int(input("Por favor, ingrese el segundo valor del rango (limite superior): \n"))

# print(f"borde izquierdo: {borde_izquierdo}")
# print(f"borde derecho: {borde_derecho}")

if not borde_izquierdo < borde_derecho:
    print(f"El segundo valor del rango ({borde_derecho}) debe ser OBLIGATORIAMENTE mayor al primer valor ({borde_izquierdo}).")
    exit()

numero_aleatorio = randint(borde_izquierdo, borde_derecho)
# print(f"Valor aleatorio generado: {numero_aleatorio}")

# Si el numero aleatorio no es par
if not numero_aleatorio % 2 == 0:
    # print("Numero aleatorio impar")
    # Si el siguiente en la secuencia para ser el numero aleatorio está en el rango se suma 1
    if (numero_aleatorio + 1) <= borde_derecho:
        # print("El siguiente par está en el rango")
        numero_aleatorio += 1
        # print(f"Valor aleatorio par: {numero_aleatorio}")

    else:
        # Si el siguiente en la secuencia para ser el numero aleatorio se sale del rango se resta 1
        # print("El siguiente par no está en el rango")
        numero_aleatorio -= 1
        # print(f"Valor aleatorio par: {numero_aleatorio}")

print("=" * 34)
print("=" * 8 + " " + "¡¡¡LET'S PLAY!!!" + " " + "=" * 8)
print("=" * 34)

while veces_intentadas < CANTIDAD_MAXIMA_INTENTOS:
    if (veces_intentadas > 0):
        valor_intentado_usuario = int(input("Intenta adivinar de nuevo el número generado :p \n:"))
    else:
        valor_intentado_usuario = int(input("Intenta adivinar el número generado :p \n:"))

    distancia_intento_previo = abs(numero_aleatorio - valor_intento_previo)
    # print(f"Distancia del intento previo: {distancia_intento_previo}")

    distancia_intento_actual = abs(numero_aleatorio - valor_intentado_usuario)
    # print(f"Distancia del intento actual: {distancia_intento_actual}")

    if valor_intentado_usuario < borde_izquierdo or valor_intentado_usuario > borde_derecho:
        print(f"El valor ingresado debe estar dentro del rango (mayor o igual a {borde_izquierdo} y menor o igual a {borde_derecho}).")
        continue

    # print(f"El valor intentado es: {valor_intentado_usuario}")

    if valor_intentado_usuario == numero_aleatorio:
        print(f"Felicitaciones!! Has adivinado en tu intento N°{veces_intentadas + 1}.")
        exit()

    if valor_intentado_usuario < numero_aleatorio:
        print(f"El número a adivinar es menor.")

    else:
        print(f"El número a adivinar es mayor.")

    print(f"Te dare una pista:")
    if distancia_intento_previo < distancia_intento_actual:
        print(f"El número que buscas está más cerca de {valor_intento_previo} que de {valor_intentado_usuario}.")
    else:
        print(f"El número que buscas está más cerca de {valor_intentado_usuario} que de {valor_intento_previo}.")

    valor_intento_previo = valor_intentado_usuario
    veces_intentadas += 1

print("Has alcanzado el maximo de intentos, mejor suerte la proxima WAJAJAJ :p")
print(f"El número a adivinar era: {numero_aleatorio}")