import sqlite3

# 1. Nos conectamos al mismo archivo
conexion = sqlite3.connect('f1_telemetria.db')
cursor = conexion.cursor()

# 2. Escribimos la consulta SQL para traer TODO (*) de la tabla
cursor.execute("SELECT * FROM telemetria")

# 3. Le pedimos al cursor que recupere todas las filas encontradas
filas = cursor.fetchall()

# 4. Recorremos las filas con un bucle for para mostrarlas en la terminal
print("--- DATOS DENTRO DE LA BASE DE DATOS ---")
for fila in filas:
    print(fila)

conexion.close()