import sqlite3

conexion = sqlite3.connect('f1_telemtria.db')

print("¡Conexion exitosa con la base de datos!")

conexion.close()