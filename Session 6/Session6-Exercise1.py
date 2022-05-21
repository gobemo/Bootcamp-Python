## This is exercise 1 session 5 of the Python course done at open.bootcamp.com
## Define class car
## Gonzalo Beltran Morera
## gobemo@gmail.com

class Vehiculo:
    color: str = "Negro"
    ruedas: int = 4
    puertas: int = 5

class coche (Vehiculo):
    velocidad: int = 100
    cilindrada: int = 1300

miCarro = coche()
print("El color de mi carro es: ", miCarro.color)
print("Mi carro tiene:", str(miCarro.ruedas) +" ruedas")
print("Mi carro tiene:", str(miCarro.puertas) +" ruedas")
print("Mi carro tiene una velocidad maxima de: ", str(miCarro.velocidad))
print("Mi carro tiene una cilindraje de:", str(miCarro.cilindrada))