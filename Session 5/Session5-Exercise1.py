## This is exercise 1 session 5 of the Python course done at open.bootcamp.com
## Calculation of the area of a triangle
## Gonzalo Beltran Morera
## gobemo@gmail.com

def areaTriagule():
    print("Area de un trangulo")
    alture = int (input("Ingrese la altura: "))
    base = int (input("Ingrese la base: "))
    area = alture * base
    return area

def areaCircle():
    print("Area de un circulo: ")
    radio = int (input("Ingrese el radio: "))
    area = 3.1416 * (radio**2) 
    return area

def menu_screen():
    print("Ingrese 1 para determinar el area de un triangulo")
    print("Ingrese 2 para determinar el area de un circulo")
    print("Ingrese 3 para salir")
    
menu = 1
while (menu != 0):
    menu_screen()
    opcion = int (input("Opcion: "))
    if opcion == 1:
        Triangle = areaTriagule()
        print("El area del Triagulo es ", Triangle) 

    elif opcion == 2:
        Circule = areaCircle()
        print("El area del Circulo es ", Circule)
    
    elif opcion == 3:
        break
    else:
        print("Ingrese una opcion valida")


