def buscar_valor(matriz, valor):
    """Busca un valor en la matriz y devuelve su posición (fila, columna)"""
    for i in range(3):  # Recorre las filas
        for j in range(3):  # Recorre las columnas
            if matriz[i][j] == valor:
                return (i, j)  # Devuelve la posición si encuentra el valor
    return None  # Devuelve None si no se encuentra

# Matriz 3x3 con valores numéricos
matriz = [
    [4, 9, 2],
    [3, 5, 7],
    [8, 1, 6]
]

# Mostrar la matriz
print("📌 Matriz:")
for fila in matriz:
    print(fila)

# Pedir al usuario un valor a buscar
valor_a_buscar = int(input("\n🔍 Ingrese el valor a buscar en la matriz: "))

# Llamar a la función de búsqueda
posicion = buscar_valor(matriz, valor_a_buscar)

# Mostrar el resultado
if posicion:
    print(f"\n✅ El valor {valor_a_buscar} se encontró en la posición (fila {posicion[0]}, columna {posicion[1]}).")
else:
    print(f"\n❌ El valor {valor_a_buscar} no se encuentra en la matriz.")