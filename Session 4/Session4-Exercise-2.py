## This is exercise 1 session 4 of the Python course done at open.bootcamp.com
## Printing odd numbers
## Gonzalo Beltran Morera
## gobemo@gmail.com

flack = 0

while (flack == 0):

    ini = int (input("El primer numero: "))
    end = int (input("Ingrese el Numero final:"))

    if ini < end:
        for i in range(ini, end):
            if i % 2 != 0:
                print (i)
                flack = 1
    else:
        print ("El numero inicial debe ser menor al final")

