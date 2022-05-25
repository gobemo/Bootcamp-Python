sqlite3 colegio.db

CREATE TABLE alumnos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    apellido TEXT NOT NULL);

INSERT INTO alumnos (nombre, apellido) VALUES ('Gonzalo','Beltran');
INSERT INTO alumnos (nombre, apellido) VALUES ('Juan Felipe','Beltran');
INSERT INTO alumnos (nombre, apellido) VALUES ('Catalina','Ciro');
INSERT INTO alumnos (nombre, apellido) VALUES ('Ramon','Valdez');
INSERT INTO alumnos (nombre, apellido) VALUES ('Patricia','Fernandez');
INSERT INTO alumnos (nombre, apellido) VALUES ('Hermes','Santos');
INSERT INTO alumnos (nombre, apellido) VALUES ('Humberto','Celis');
INSERT INTO alumnos (nombre, apellido) VALUES ('Julio','Pequeño');

SELECT * FROM alumnos WHERE nombre = {nombre}