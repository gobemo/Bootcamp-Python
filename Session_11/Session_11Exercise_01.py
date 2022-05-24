import sqlite3

def run():
    def crearTabla():
        ##Abrir coexiones
        conn = sqlite3.connect('colegio.db')
        cursor =  conn.cursor()

        ##Creación Tabla
        cursor.execute ("CREATE TABLE alumnos (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT NOT NULL, apellido TEXT NOT NULL);")

        ##Insercion de datos
        cursor.execute ("INSERT INTO alumnos (nombre, apellido) VALUES ('Gonzalo','Beltran');")
        cursor.execute ("INSERT INTO alumnos (nombre, apellido) VALUES ('Juan Felipe','Beltran');")
        cursor.execute ("INSERT INTO alumnos (nombre, apellido) VALUES ('Catalina','Ciro');")
        cursor.execute ("INSERT INTO alumnos (nombre, apellido) VALUES ('Ramon','Valdez');")
        cursor.execute ("INSERT INTO alumnos (nombre, apellido) VALUES ('Patricia','Fernandez');")
        cursor.execute ("INSERT INTO alumnos (nombre, apellido) VALUES ('Hermes','Santos');")
        cursor.execute ("INSERT INTO alumnos (nombre, apellido) VALUES ('Humberto','Celis');")
        cursor.execute ("INSERT INTO alumnos (nombre, apellido) VALUES ('Julio','Pequeño');")
        conn.commit()
        ##Cerrar conexiones
        cursor.close()
        conn.close()

    def imprime_datos():
        #Abrir la Base de datos
        conn = sqlite3.connect('colegio.db')
        cursor =  conn.cursor()
        #Realiza la consulta
        query = f'SELECT * FROM alumnos WHERE nombre = "Gonzalo";'
        cursor.execute(query)
        datos = cursor.fetchall()
        ##Muestra los datos
        print(datos)

        
    crearTabla()
    imprime_datos()


if __name__ == '__main__':
    run()


