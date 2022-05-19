## This is exercise 1 session 5 of the Python course done at open.bootcamp.com
## Validate if a number is prime 
## Gonzalo Beltran Morera
## gobemo@gmail.com

def saberPrimo(primo):
    for i in range(2,primo):
        if primo % i == 0:
            return False
            break
    return True
   
primo = int (input("Ingrese un numero para determinar si es primo: "))

validar = saberPrimo(primo)

if validar == True:
    print("El numero  es primo")
else:
    print("El numero  NO es primo")
