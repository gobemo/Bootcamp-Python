
import tkinter

def run():

    def resetarvalores ():
        radio_1.deselect()
        radio_2.deselect()
        radio_3.deselect()
        radio_4.deselect()
        radio_5.deselect()

    window = tkinter.Tk()
    #Geometría
    radioValue = tkinter.IntVar()
    
    radio_1 = tkinter.Radiobutton(window,text = 'Lunes',variable=radioValue, value = 1)
    radio_2 = tkinter.Radiobutton(window,text = 'Martes',variable=radioValue, value = 2)
    radio_3 = tkinter.Radiobutton(window,text = 'Miercoles',variable=radioValue, value = 3)
    radio_4 = tkinter.Radiobutton(window,text = 'Jueves',variable=radioValue, value = 4)
    radio_5 = tkinter.Radiobutton(window,text = 'Viernes',variable=radioValue, value = 5)

    radio_1.grid(column=0,row=1)
    radio_2.grid(column=0,row=2)
    radio_3.grid(column=0,row=3)
    radio_4.grid(column=0,row=4)
    radio_5.grid(column=0,row=5) 

    boton = tkinter.Button(window,width=3,height=3,text='Reset',command=resetarvalores)
    boton.grid (column=0,row=7)

    window.mainloop()

if __name__ == '__main__':
    run()
