#Se que se puede hacer con menos lineas, pero aqui entendi que estoy haciendo paso a paso

def run():
    #Ingresar la información
    paises = input('Ingrese varios paises, separados por cor coma: ')
    #Agregar una lista agregando un elemento por cada coma que encuentre
    paises = paises.split(',')
    #Eliminar los valores repetidos
    paises_no_repetidos = list(set(paises))
    #Ordenar la lista alfabeticamente
    paises_no_repetidos = sorted(paises_no_repetidos)
    #Imprimir la lista de cada elemento separado por coma
    print(f','.join(list(paises_no_repetidos)))


    

if __name__ == '__main__':
    run()
