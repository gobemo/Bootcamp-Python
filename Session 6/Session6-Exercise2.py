## This is exercise 1 session 5 of the Python course done at open.bootcamp.com
## Define class student
## Gonzalo Beltran Morera
## gobemo@gmail.com

#Inicializar la clase

class Alumno():
    #Inicializacion de atributos
    def inicio (self,nombre, nota):
        self.nombre = nombre
        self.nota = nota
    
    def impresion (self):
        print ("El nombre es", self.nombre)
        print ("La nota es: ", self.nota)
    
    def obtencion(self):
        if self.nota >=6:
            print ("Felicidades el alumno aprobo")
        else:
            print ("El alumno reprobo")

#Insercion de tres alumnos

alumno01 = Alumno()
Alumno02 = Alumno()

#Agregar datos
alumno01.inicio("Juan", 8)
Alumno02.inicio("Carlos", 3)

#Imprimir datos
alumno01.impresion()
alumno01.obtencion()
Alumno02.impresion()
Alumno02.obtencion()

