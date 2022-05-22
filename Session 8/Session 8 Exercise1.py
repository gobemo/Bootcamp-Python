

def run():
    archivo = open('example.txt','w')
    archivo.write('Primer ingreso \n')
    archivo.close()

    archivo = open('example.txt','a')
    archivo.write('Segundo ingreso \n')
    archivo.close()

if __name__ == '__main__':
    run()
