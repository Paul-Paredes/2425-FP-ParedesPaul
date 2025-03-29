# TAREA: Trabajando con Diccionarios en Python

# 1. Crear un diccionario con información ficticia
informacion_personal = {
    "nombre": "Fernando",
    "edad": 38,
    "ciudad": "Guayaquil",
    "profesion": "Abogado"
}

# 2. Acceder y modificar el valor de la clave "ciudad"
informacion_personal["ciudad"] = "Cuenca"

# 3. Agregar una nueva clave-valor para la profesión (reemplazamos o actualizamos)
informacion_personal["profesion"] = "Doctor en leyes"

# 4. Verificar si la clave "telefono" existe, y si no, agregarla
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0987654321"

# 5. Eliminar la clave "edad"
if "edad" in informacion_personal:
    del informacion_personal["edad"]

# 6. Imprimir el diccionario final
print("Diccionario final:")
print(informacion_personal)