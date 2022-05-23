
import tkinter
from tkinter import Label, ttk

def run():

    window = tkinter.Tk()
    #Geometría
    window.geometry('300x190')

    titulo =  Label(window,text='Selecciona que dia quieres descansar')
    titulo.place(x = 30, y= 50)
    lista_desplegable = ttk.Combobox(window, width=17)
    lista_desplegable.place (x=30, y=77)

    opciones = ['Lunes','Martes','Miercoles','Jueves','Viernes']

    lista_desplegable ['values'] = opciones

    window.mainloop()

if __name__ == '__main__':
    run()
