import getpass
import sqlite3

conn = sqlite3.connect('colegio.db')
cursor =  conn.cursor()
nombre = input('Ingrese el nombre a buscar: ')
rows = cursor.execute(f'SELECT * FROM alumnos WHERE nombre = "{nombre}"')
validador = rows.fetchone()
resultado = rows.fetchall()

if validador == None:
    print('No existen datos para mostrar')
else:
    print(resultado)

cursor.close()
##Cerrar la base de datos
conn.close()


