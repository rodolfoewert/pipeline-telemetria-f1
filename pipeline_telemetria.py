import sqlite3

conexion = sqlite3.connect('f1_telemetria.db')

cursor = conexion.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS telemetria (
        piloto TEXT,
        vuelta INTEGER,
        velocidad_max REAL, 
        tiempo_vuelta REAL
        )
''')
datos_carrera = [
    ('Verstappen', 1, 325.4, 78.5),
    ('Hamilton', 1, 322.1, 79.2),
    ('Verstappen', 2, 328.0, 77.9),
    ('Hamilton', 2, 324.5, 78.1)
]

cursor.executemany('''
        INSERT INTO telemetria (piloto, vuelta, velocidad_max, tiempo_vuelta)
        VALUES (?, ?, ?, ?)
''', datos_carrera)

conexion.commit()

print("¡Conexion exitosa con la base de datos!")

conexion.close()