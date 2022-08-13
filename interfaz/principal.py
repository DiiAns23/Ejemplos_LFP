from tkinter import *
from tkinter import ttk

''' PANTALLA PRINCIPAL DE LA APLCIACION'''
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
        self.secundaria = True
