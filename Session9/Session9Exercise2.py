from functools import reduce

def run():
    numeros = [0,1,2,3,4,5,6,7,8,9,10]

    def impares(x):
        if x % 2 != 0:
            return True
        return False
    
    def suma(x, y):
        return x + y

    ##FUNCION FILTER
    resultado = list(filter(impares, numeros))
    print (list(resultado))
    #Resultado con funcion
    resultado1 = reduce(suma, resultado)
    print(f'resultado con una funcion {resultado1}')
    #Operacion con lambda
    resultado2 = reduce(lambda x, y: x + y ,resultado)
    print(f'resultado con lambda {resultado2}')

if __name__ == '__main__':
    run()
