"""
Programa: Reserva de asientos de sala de cine
Autor: Fernanda Tipán
Objetivo: Gestionar la reserva de un asiento en una sala de cine de 3 filas por 4 columnas, usando una matriz.
          El programa pide al usuario la fila y columna del asiento a reservar, lo marca con 1 (reservado) y 
          luego muestra el estado completo de la sala.
"""

# Cantidad de filas y columnas de la sala
NUM_FILAS = 3
NUM_COLUMNAS = 4

# 1. Crear la matriz "asientos" de 3x4, todos inicializados en 0 (libre)
asientos = []
for i in range(NUM_FILAS):
    fila_actual = [0] * NUM_COLUMNAS  # crea una fila de 4 ceros
    asientos.append(fila_actual)

# 2. Pedir al usuario la fila y columna del asiento que desea reservar
fila = int(input("Ingrese fila (0 a 2): "))
columna = int(input("Ingrese columna (0 a 3): "))

# Validación opcional: verificar que la fila y columna estén en rango
if fila < 0 or fila >= NUM_FILAS or columna < 0 or columna >= NUM_COLUMNAS:
    print("Error: fila o columna fuera de rango.")
else:
    # Validación opcional: avisar si el asiento ya estaba reservado
    if asientos[fila][columna] == 1:
        print("Aviso: ese asiento ya estaba reservado.")
    else:
        # 3. Marcar el asiento como reservado (1)
        asientos[fila][columna] = 1
        print("Asiento reservado con éxito.")

    # 4. Mostrar la matriz completa en formato de tabla con bucles anidados
    print("Estado de la sala:")
    for i in range(NUM_FILAS):
        for j in range(NUM_COLUMNAS):
            print(asientos[i][j], end=" ")  # sin salto de línea entre columnas
        print()  # salto de línea al terminar cada fila