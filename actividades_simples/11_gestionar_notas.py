notas = []
total_notas = 0.0
promedio_final = 0.0

"""
for i in range(0, 5):
    try:
        nota_raw = float(input(f"Por favor, ingrese la nota #{i + 1}.\n:"))
    except ValueError:
        nota_raw = 0

    notas.append(nota_raw)
    total_notas += nota_raw

promedio_final = total_notas/len(notas)

print(f"El promedio final es: {promedio_final:.2f}")

notas.clear()
total_notas = 0.0
promedio_final = 0.0
"""

MAX_CANTIDAD_NOTAS = 5
nota_actual = 0

while nota_actual < MAX_CANTIDAD_NOTAS:
    try:
        nota_raw = float(input(f"Por favor, ingrese la nota #{nota_actual + 1}.\n:"))
    except ValueError:
        nota_raw = 0

    notas.append(nota_raw)
    total_notas += nota_raw

    nota_actual += 1

promedio_final = total_notas/len(notas)
print(f"El promedio final es: {promedio_final:.2f}")

