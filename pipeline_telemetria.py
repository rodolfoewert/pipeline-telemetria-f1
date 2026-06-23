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
    # Red Bull Racing
    ('Verstappen', 1, 325.4, 78.5),
    ('Verstappen', 2, 328.0, 77.9),
    ('Perez', 1, 322.5, 79.1),
    ('Perez', 2, 324.8, 78.6),
    
    # Mercedes-AMG
    ('Hamilton', 1, 322.1, 79.2),
    ('Hamilton', 2, 324.5, 78.1),
    ('Russell', 1, 323.0, 79.0),
    ('Russell', 2, 325.2, 78.3),
    
    # Ferrari
    ('Leclerc', 1, 326.1, 78.2),
    ('Leclerc', 2, 329.4, 77.6),
    ('Sainz', 1, 324.0, 78.8),
    ('Sainz', 2, 327.1, 78.0),
    
    # McLaren
    ('Norris', 1, 324.8, 78.4),
    ('Norris', 2, 327.9, 77.7),
    ('Piastri', 1, 323.5, 78.9),
    ('Piastri', 2, 326.0, 78.2),
    
    # Aston Martin
    ('Alonso', 1, 321.8, 79.8),
    ('Alonso', 2, 324.2, 78.4),
    ('Stroll', 1, 320.5, 80.2),
    ('Stroll', 2, 322.9, 79.1),
    
    # Alpine
    ('Gasly', 1, 319.8, 80.5),
    ('Gasly', 2, 322.1, 79.4),
    ('Ocon', 1, 319.2, 80.7),
    ('Ocon', 2, 321.8, 79.6)
]

cursor.executemany('''
        INSERT INTO telemetria (piloto, vuelta, velocidad_max, tiempo_vuelta)
        VALUES (?, ?, ?, ?)
''', datos_carrera)

conexion.commit()

print("¡Conexion exitosa con la base de datos!")

conexion.close()