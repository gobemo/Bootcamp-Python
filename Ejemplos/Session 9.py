##Para usar reduca de debe importar esta libreria
from audioop import reverse
from functools import reduce

def run():
    numeros = [0,1,2,3,4,5,6,7,8,9,10]
    nombres = ['pepe','cuchillo', 'peperoni','papa']
    cursos = ['Java','Python','Git']
    alumnos = ['Juan', 'Valentina', 'Catalina']

    def mifuncion(x):
        if x % 2 == 0:
            return True
        return False
    
    def mifuncionLetras(y):
        if str(y).startswith('pep'):
            return True
        return False

    def cuadrado(x):
        return x * x
    
    def suma(x, y):
        return x + y
    
    def suma_validacion(x, y):
        print(f'x = {x}, y = {y}')
        return x + y

    ##FUNCION FILTER
    # si el resultado de la funcion es Falso lo eliminará
    resultado = filter(mifuncion, numeros)
    print (list(resultado))

    #Realizada con una lambda
    resultado2 = filter(lambda x: x % 2 == 0, numeros)
    print(list(resultado2))

    #Realizada con una lista de nombres
    resultado3 = filter(mifuncionLetras,nombres)
    print(list(resultado3))

    #Realizada con Lambda utilizando nombres
    resultado4 = filter(lambda x: str(x).startswith('pep'),nombres)
    print(list(resultado4))

    #FUNCION MAP, 
    # Aplica la funcion a todos elementos de la lista o Tupla

    resultado5 = map(cuadrado,numeros)
    print(list(resultado5))

    #Funcion MAP, con lambda
    resultado6 = map(lambda x : x * x,numeros)
    print(list(resultado6))

    #FUNCION REDUCE
    #Se aplicara un unico resultado
    #hasta que la lista quede con un solo elemento
    resultado7 = reduce(suma, numeros)
    print(resultado7)

    #Aplicando Lambda
    resultado8 = reduce(lambda x, y: x + y ,numeros)
    print(resultado8)

    #Revisando como funciona el reduce
    resultado9 = reduce(suma_validacion, numeros)
    print(resultado9)

    #Aplicando Lambda
    resultado10 = reduce(lambda x, y: x + y ,numeros)
    print(resultado8)

    #ZIP asocia uno a uno en una tupla

    zip1 = zip(cursos, alumnos)
    print(list(zip1))

    ## all y any
    # any valida que por lo menos un elemento de la lista sea verdadera
    # all valida que todas sean verdaderas

    Lista1 = [1 == 1, 2 == 2, 3 == 4]
    Lista2 = [1 == 1, 2 == 2, 3 == 3]
    analisis = any(Lista1)
    print(analisis)

    analisis1 = all(Lista1)
    print(analisis1)

    analisis2 = all(Lista2)
    print(analisis2)

    #Funcion Round menor o igual a .5 redonde hacia abajo, los demas hacia arriba
    a = 5.5
    b = 5.4
    c = 5.9

    print (f'Numeros {round(a)}, {round(b)}, {round(c)}')

    print (f'El min imprime el valor minimo {min(3,6,3,6,8,5,6,8,1)}')

    print (f'Para elevar usamos pow {pow(6,8)}')

    #Ordenar una lista con sorted
    lista_prueba = ['origen', 'fin','en medio', 'atras', 'policia','madre']
    ordenada = sorted(lista_prueba)
    orden_reves = sorted(lista_prueba,reverse = True)
    print (f'Lista sin ordenar {list(lista_prueba)}')
    print (f'Lista ordenada {list(ordenada)}')
    print (f'Lista ordenada al reves {list(orden_reves)}')
    
    #PAra agregar una condicion, ejemplo se usa una lambda para que la 
    # primera paabra que empieza por b salga de primero, asi la instruccion 
    # es uq ela lista se muestre al reves
    #key= lambda x: str(x).startswith('f')

    lista_prueba1 = ['o', 'f','e', 'a', 'p','m']

    print(list(lista_prueba1))

    orde_lambda = sorted(lista_prueba1, reverse = True)
    orde_lambda2 = sorted(orde_lambda, key= lambda x: str(x).startswith('f'),reverse = True)
    print (f'Lista ordenada al reves con una condicion {list(orde_lambda2)}')

    ## Funcion input
    # Asigna un valor a una variable

    e = input('Cual es tu nombre')
    print(f'Hola {e}')

if __name__ == '__main__':
    run()
