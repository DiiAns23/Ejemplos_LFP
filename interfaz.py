from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

''' PANTALLA PRINCIPAL '''
class PantPrin():
    def __init__(self):
        self.ventana = Tk()
        self.ventana.resizable(True,False)
        self.ventana.title('Practica 1 LFP B+')
        self.Centrar(self.ventana, 600, 500)
        self.ventana.geometry('600x500')
        self.ventana.configure(bg='#102027')
        self.Ventana()

    def Centrar(self, r, ancho, alto):
        altura_pantalla = r.winfo_screenheight()
        ancho_pantalla = r.winfo_screenwidth()

        x = (ancho_pantalla // 2) - (ancho // 2)
        y = (altura_pantalla // 2) - (alto // 2)
        r.geometry(f'+{x}+{y}')

    def Ventana(self):
        self.frame = Frame(height=500, width=400)
        self.frame.config(bg='#37474f')
        self.frame.pack(padx=25, pady=25)
        Label(self.frame, text="Primera Pantalla", font=('Times New Roman',15), fg='#000000', bg='#ff6f00', width=20).place(x=80, y=50)
        Button(self.frame, text="Abrir", command=self.IrPantalla2 , font=('Times New Roman',15), fg='#000000', bg='#ff6f00', width=10).place(x=130, y=100)
        self.frame.mainloop()
    
    def IrPantalla2(self):
        self.ventana.destroy()
        PantSec()


''' SEGUNDA PANTALLA '''
class PantSec():
    def __init__(self):
        self.ventana = Tk()
        self.ventana.resizable(True,False)
        self.ventana.title('Segunda Pantalla')
        self.Centrar(self.ventana, 600, 500)
        self.ventana.geometry('600x500')
        self.ventana.configure(bg='#102027')
        self.Ventana()
    
    def Centrar(self, r, ancho, alto):
        altura_pantalla = r.winfo_screenheight()
        ancho_pantalla = r.winfo_screenwidth()

        x = (ancho_pantalla // 2) - (ancho // 2)
        y = (altura_pantalla // 2) - (alto // 2)
        r.geometry(f'+{x}+{y}')

    def Ventana(self):
        self.frame = Frame(height=500, width=400)
        self.frame.config(bg='#37474f')
        self.frame.pack(padx=25, pady=25)
        Label(self.frame, text="Segunda Pantalla", font=('Times New Roman',15), fg='#000000', bg='#ff6f00', width=20).place(x=80, y=50)
        Button(self.frame, text="Abrir",command=self.IrPantalla1, font=('Times New Roman',15), fg='#000000', bg='#ff6f00', width=10).place(x=130, y=100)

        tabla = ttk.Treeview(self.frame, columns=('#0','#1','#2'), height=7)

        style = ttk.Style()
        style.configure(
            'Treeview',
            background = 'silver',
            foreground = 'black',
            rowheight = 25,
            fielbackground = 'silver'
        )
        style.map(
            'Treeview',
            background = [('selected', 'green')]
        )

        tabla.grid(row=0, column=0, columnspan=2)
        tabla.column('#0', width = 100)
        tabla.column('#1', width = 100, anchor = CENTER)
        tabla.column('#2', width = 100, anchor = CENTER)
        tabla.column('#3', width = 100, anchor = CENTER)

        tabla.heading("#0", text = 'Carne', anchor = CENTER)
        tabla.heading("#1", text = 'Nombre', anchor = CENTER)
        tabla.heading('#2', text = 'Apellido', anchor = CENTER)
        tabla.heading('#3', text = 'Edad', anchor = CENTER)
        ## AQUI SE MANDA A LLAMAR A LA FUNCION QUE NOS DEVUELVE TODOS LOS CURSOS
        
        tabla.insert("",END, text='Carne 1', values=('Nombre 1', 'Apellido 1', 'Edad 1'))
        tabla.insert("",END, text='Carne 2', values=('Nombre 2', 'Apellido 2', 'Edad 2'))
        tabla.insert("",END, text='Carne 3', values=('Nombre 3', 'Apellido 3', 'Edad 3'))
        tabla.insert("",END, text='Carne 4', values=('Nombre 4', 'Apellido 4', 'Edad 4'))
        
        self.frame.mainloop()

    def IrPantalla1(self):
        self.ventana.destroy()
        PantPrin()

PantPrin()