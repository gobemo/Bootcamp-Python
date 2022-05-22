from json import load
import pickle

#Crear la clase
class Vehiculo:
    color: str = "Negro"
    ruedas: int = 4
    puertas: int = 5

    #Funcion de asignar valores a la clase

    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas
    
    #Funcion de imprimir los datos de la clase

    def datosAuto(self):
        return self.color, self.ruedas, self.puertas

def run():
    #Asignar datos a la clase Vehiculo
    auto = Vehiculo('rojo',4,2)

    #Crear el archivo y guardarlo
    archivo = open('vehiculo','wb')
    pickle.dump(auto, archivo)
    archivo.close()

    #Cargar informacion del archivo

    archivo = open('vehiculo','rb')
    revision = pickle.load(archivo)
    print(revision.datosAuto())
    archivo.close()

if __name__ == '__main__':
    run()


