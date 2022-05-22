import calculadora as c


numero1 = int(input("Ingrese el numero 1: "))
numero2 = int(input("Ingrese el numero 2: "))

resultado_suma = c.sumar(numero1,numero2)
print("La suma es de: ",resultado_suma)

resultado_resta = c.restar(numero1,numero2)
print("La resta es de: ",resultado_resta)

resultado_mult = c.multiplicar(numero1,numero2)
print("La multiplicacion es de: ",resultado_mult)

resultado_divi = c.dividir(numero1,numero2)
print("La division es de: ",resultado_divi)

