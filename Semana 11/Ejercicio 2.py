def bubble_sort(fila):
    """Ordena una lista (fila de la matriz) usando Bubble Sort"""
    n = len(fila)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]  # Intercambio de valores

# Definir una matriz 3x3 con valores numéricos desordenados
matriz = [
    [12, 5, 8],
    [7, 3, 9],
    [4, 10, 6]
]

# Mostrar la matriz original
print("📌 Matriz original:")
for fila in matriz:
    print(fila)

# Elegir la fila a ordenar (por ejemplo, la segunda fila - índice 1)
fila_a_ordenar = 1

# Aplicar Bubble Sort en la fila seleccionada
bubble_sort(matriz[fila_a_ordenar])

# Mostrar la matriz después de ordenar la fila
print("\n✅ Matriz después de ordenar la fila seleccionada:")
for fila in matriz:
    print(fila)