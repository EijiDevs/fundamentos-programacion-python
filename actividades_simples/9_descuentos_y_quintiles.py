DIECIOCHO_PORCIENTO = 0.18
OCHO_PORCIENTO = 0.08
DOCE_PORCIENTO = 0.12
DIEZ_PORCIENTO = 0.1
CINCO_PORCIENTO = 0.05

precio_base_plan_dental = 80000
precio_base_radiografia_dental = 12000

porcentaje_descuento_plan_dental = 0.0
porcentaje_descuento_radiografia_dental = 0.0

monto_descuento_plan_dental = 0
monto_descuento_radiografia_dental = 0

valor_final_radiografia_dental = 0
valor_final_plan_dental = 0

print("=" * 53)
print("=" * 8 + " " + "CALCULO DE PLANES DE CLINICA DENTAL" + " " + "=" * 8)
print("=" * 53)

usuario_edad = int(input("Por favor, ingrese su edad:\n"))

if usuario_edad < 0:
    print("Por favor ingrese su edad en años con un valor mayor o igual 0.")
    exit()

usuario_quintil = int(input("Por favor, ingrese el quintil al que pertenece (1 a 5):\n"))

if usuario_quintil not in range(1, 6):
    print("Por favor seleccione una opción valida entre 1 a 5.")
    exit()

if usuario_edad <= 25:
    # Calculo porcentaje descuento de plan dental
    if usuario_quintil == 1 or usuario_quintil == 2:
        porcentaje_descuento_plan_dental += DIECIOCHO_PORCIENTO

    if usuario_quintil == 3 or usuario_quintil == 4:
        porcentaje_descuento_plan_dental += DOCE_PORCIENTO

    # Calculo porcentaje descuento de radiografia dental
    if usuario_quintil == 1 or usuario_quintil == 2 or usuario_quintil == 3:
        porcentaje_descuento_radiografia_dental += DIEZ_PORCIENTO

        if usuario_edad >= 40:
            # Si tiene 40 o más años se aplica un 5% adicional
            porcentaje_descuento_radiografia_dental += CINCO_PORCIENTO

elif 26 <= usuario_edad <= 45:
    # Calculo porcentaje descuento de plan dental
    if usuario_quintil == 1 or usuario_quintil == 2:
        porcentaje_descuento_plan_dental += DOCE_PORCIENTO

    if usuario_quintil == 3 or usuario_quintil == 4:
        porcentaje_descuento_plan_dental += OCHO_PORCIENTO

    # Calculo porcentaje descuento de radiografia dental
    if usuario_quintil == 1 or usuario_quintil == 2 or usuario_quintil == 3:
        porcentaje_descuento_radiografia_dental += DIEZ_PORCIENTO

        if usuario_edad >= 40:
            # Si tiene 40 o más años se aplica un 5% adicional
            porcentaje_descuento_radiografia_dental += CINCO_PORCIENTO

# print(f"El porcentaje a descontar para el plan dental es: {porcentaje_descuento_plan_dental} \n")
# print(f"El porcentaje a descontar para la radiografia dental es: {porcentaje_descuento_radiografia_dental} \n")

# Calculo monto a descontar del plan dental
monto_descuento_plan_dental = precio_base_plan_dental * porcentaje_descuento_plan_dental
# print(f"El monto a descontar para el plan dental es: {monto_descuento_plan_dental} \n")

# Calculo monto a descontar de la radiografia dental
monto_descuento_radiografia_dental = precio_base_radiografia_dental * porcentaje_descuento_radiografia_dental
# print(f"El monto a descontar para la radiografia dental es: {monto_descuento_radiografia_dental} \n")

# Calculo valor final del plan dental
valor_final_plan_dental = precio_base_plan_dental - monto_descuento_plan_dental

# Calculo valor final de la radiografia dental
valor_final_radiografia_dental = precio_base_radiografia_dental - monto_descuento_radiografia_dental

# Caso para mayores de 45 años, no cuentan con descuento
print(f"El valor del plan dental es: {int(valor_final_plan_dental)}")

print(f"El valor de la radiografia dental es: {int(valor_final_radiografia_dental)}")

