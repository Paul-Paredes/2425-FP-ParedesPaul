# --- Escritura de Archivo de Texto ---

# Abrimos (o creamos) el archivo en modo escritura ('w')
archivo = open("my_notes.txt", "w")

# Escribimos tres líneas de notas personales (versiones diferentes)
archivo.write("Hoy descubrí que programar es como resolver acertijos interesantes.\n")
archivo.write("Hoy llovió mucho, pero aproveché para estudiar en casa.\n")
archivo.write("Cada línea de código me hace sentir más seguro en lo que aprendo.\n")

# Cerramos el archivo después de escribir
archivo.close()


# --- Lectura del Archivo de Texto ---

# Abrimos el archivo en modo lectura ('r')
archivo = open("my_notes.txt", "r")

# Leemos línea por línea usando un bucle
print("Contenido del archivo:")
linea = archivo.readline()
while linea:
    print(linea.strip())  # .strip() elimina saltos de línea adicionales al imprimir
    linea = archivo.readline()

# Cerramos el archivo después de leer
archivo.close()