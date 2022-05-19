## This is exercise 1 session 5 of the Python course done at open.bootcamp.com
## Define whether a year is a leap year
## Gonzalo Beltran Morera
## gobemo@gmail.com

def bisiesto(year):
    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
        return True
    else:
        return False
   
year = int (input("Ingrese un año para validar si es bisiesto: "))

validar = bisiesto(year)

if validar == True:
    print("El año es bisiesto")
else:
    print("El año NO es bisiesto")
