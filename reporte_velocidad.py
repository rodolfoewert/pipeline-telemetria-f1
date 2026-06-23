import sqlite3

conexion = sqlite3.connect('f1_telemetria.db')
cursor = conexion.cursor()

consulta_analitica = '''
    SELECT piloto, AVG(velocidad_max) AS velocidad_promedio
    FROM telemetria
    GROUP BY piloto;
'''

cursor.execute(consulta_analitica)
resultados = cursor.fetchall()

print("--- REPORTE DE VELOCIDAD PROMEDIO (F1) ---")
for fila in resultados:
    piloto = fila [0]
    promedio = fila [1]
    print(f"Piloto: {piloto: <12} | Vel. Max. Promedio: {promedio:.1f} km/h")

conexion.close()