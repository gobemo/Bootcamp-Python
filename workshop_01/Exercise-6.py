## This is exercise 6 of the Python course done at open.bootcamp.com
## Create variables
## Gonzalo Beltran Morera
## gobemo@gmail.com

masa: float
peso = float(input("Ingrese su peso en kilos: "))
altura = float(input("Ingrese su altura en metros: "))
masa = peso / altura
print("Su masa corporal es de: {:.2f}".format(masa))
