# PROGRAMA PARA EL CASO DE USO DE "COMPRAR UN PRODUCTO"
from enum import Enum
import time

class CondicionPago(Enum):
    EFECTIVO = 1
    DEBITO = 2
    CREDITO = 3
    TRANSFERENCIA = 4

def abortar(mensaje):
    print(mensaje)
    print("Abortando programa...")
    exit()

def validar_es_negativo(valor):
    if(valor < 0): raise ValueError("No se aceptan valores negativos.")

def validar_es_cero(valor):
    if(valor == 0): raise ValueError("No se acepta cero.")

print("=" * 36)
print("-" * 5, "CONFIGURACIÓN DE ENTORNO", "-" * 5)
print("=" * 36)

# CONFIGURAR ENTORNO DE VENTA
try:
    # VAMOS A INGRESAR EL PRECIO DEL PRODUCTO. EJ: 1000
    precio_producto = float(input(f"Por favor, ingrese el precio para su producto...\n"))
    validar_es_cero(precio_producto)
    validar_es_negativo(precio_producto)
    
    # VAMOS A INGRESAR EL SALDO ACTUAL EN BODEGA DEL PRODUCTO. EJ: 5
    saldo_producto = int(input(f"Por favor, ingrese el saldo actual en bodega para su producto...\n"))
    validar_es_cero(saldo_producto)
    validar_es_negativo(saldo_producto)
except ValueError as err:
    abortar(f"El valor que ha indicado no es un número valido. {err}")

print("=" * 36)
print("-" * 5, "INTERACCIÓN DE USUARIO", "-" * 5)
print("=" * 36)

# CASO DE USO: REALIZAR UNA VENTA
try:
    # INDICAR CANTIDAD A COMPRAR
    cantidad_compra_producto = int(input("Por favor, indique la cantidad de unidades que desea comprar...\n"))
    validar_es_cero(cantidad_compra_producto)
    validar_es_negativo(cantidad_compra_producto)
except ValueError:
    abortar(f"El valor que ha indicado no es un número valido. {err}")

# CALCULAR EL TOTAL
total_venta = cantidad_compra_producto * precio_producto

# INFORMAR AL USUARIO EL TOTAL
print("=" * 24, "TOTALES", "=" * 24)
print(f"Total a pagar: ${total_venta} CLP")
print("=" * 48)

try:
    # SOLICITAR CONDICIÓN DE PAGO
    print("Por favor, indique su condición de pago. Indique un número de la siguientes opciónes...")
    for condicion_pago in CondicionPago:
        print(f'{condicion_pago.value}) {condicion_pago.name}')
    seleccion_condicion_pago = CondicionPago(int(input(": ")))
except ValueError:
    abortar("El valor que ha indicado no es una condición de pago valida.")

try:
    # SOLICITAR MONTO A PAGAR
    monto_pago = float(input("Por favor, ingrese el monto a pagar...\n"))
    
    validar_es_cero(monto_pago)
    validar_es_negativo(monto_pago)
except ValueError as err:
    abortar(f"El valor que ha indicado no es un número valido. {err}")


print("=" * 64)
print("-" * 2, "POR FAVOR, ESPERE UN MOMENTO. ESTAMOS VALIDANDO SU PAGO...", "-" * 2)
print("=" * 64)

time.sleep(3)

# VALIDACIONES DE NEGOCIO

# SI EL USUARIO HA SOLICITADO MÁS CANTIDADES QUE LAS DISPONIBLES PARA VENDER, NO PERMITIR LA VENTA
if(cantidad_compra_producto > saldo_producto):
    print("Estimado cliente, la venta no ha podido ser procesada debido a que la cantidad solicitada ha excedido nuestro saldo actual en bodega, por favor, intente en otro momento...")
    print(f"Solicitado: {cantidad_compra_producto}")
    print(f"Saldo actual: {saldo_producto}")
    exit()

# SI EL MONTO PAGADO POR EL USUARIO ES INFERIOR AL MONTO A PAGAR, NO PERMITIR LA VENTA
if(monto_pago < total_venta):
    print("Estimado cliente, la venta no ha podido ser procesada debido a que el monto del pago no cubre el total para los productos solicitados. Por favor, regularice su situación e intentelo de nuevo más tarde...")
    print(f"Total: {total_venta}")
    print(f"Monto pagado: {monto_pago}")
    print(f"Faltan: {total_venta - monto_pago}")
    exit()

# SI LA VENTA ES POSIBLE, Y ADEMÁS EL USUARIO HA PAGADO UN MONTO IGUAL O SUPERIOR AL TOTAL A PAGAR, PERMITIR VENTA Y DEVOLVER VUELTO DE HABERLO (Total - Monto Pago)
if(monto_pago >= total_venta):
    print("Estimado cliente, estamos complacidos de informarle que su venta ha sido realizada exitosamente.")
    
    vuelto = total_venta - monto_pago

    if(vuelto > 0):
        print(f"Su vuelto es de ${vuelto} CLP")

    # REALIZAR MOVIMIENTOS DE BODEGA
    saldo_producto -= cantidad_compra_producto


# DESPEDIDA DE PROGRAMA
print("Ha sido un verdadero placer ayudarte. Gracias por elegirnos. ¡Disfruta al máximo tu experiencia y cuenta conmigo si necesitas cualquier cosa!")

# ESTADO DE BODEGA POSTERIOR A VENTA
print("-" * 16, "ESTADO DE BODEGA", "-" * 16)
print(f"Saldo restante tras venta: {saldo_producto}")
print("=" * 48)