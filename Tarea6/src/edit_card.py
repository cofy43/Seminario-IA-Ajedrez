import tkinter as tk
import tkinter.font as tkFont
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox 

class Edit_card(tk.Frame):
    def __init__(self, conector, ventana, card, *args, **kwargs):
        self.conector = conector
        self.otra_ventana = tk.Toplevel(ventana)
        self.otra_ventana.geometry("750x520")
        self.otra_ventana['bg'] = '#2196f3'
        self.card = card
        nombre = self.card[1]
        tema = self.card[2]

        nombre_label = tk.Label(self.otra_ventana, text='Nombre', bg='#2196f3', fg="black")
        nombre_label.place(x=30, y=20)
        self.nombre = tk.Entry(self.otra_ventana)
        self.nombre.insert(0, nombre)
        self.nombre.place(x=30, y=40)
        tema_label = tk.Label(self.otra_ventana, text='Tema', bg='#2196f3', fg="black")
        tema_label.place(x=30, y=80)
        self.tema = tk.Entry(self.otra_ventana)
        self.tema.insert(0, tema)
        self.tema.place(x=30, y=100)
        
        tajeta_label = tk.Label(self.otra_ventana, text='Tarjeta: ', bg='#2196f3', fg="black")
        tajeta_label.place(x=20, y = 150)
        self.tarjeta = tk.Text(self.otra_ventana, width=40, height=18)
        self.tarjeta.place(x=20, y=170)
        self.tarjeta.insert(tk.END, self.card[4])
        posicion_label = tk.Label(self.otra_ventana, text='Posición: ', bg='#2196f3', fg="black")
        posicion_label.place(x=390, y=150)
        self.font = tkFont.Font(family="Chess Cases", size=23)
        self.posicion = tk.Text(self.otra_ventana, width=16, height=9.5, font=self.font)
        self.posicion.insert(tk.END, self.card[3])
        self.posicion.place(x=390, y=170)

        self.save_edition = tk.Button(self.otra_ventana, text="Salvar edición", command = self.save, fg='white', bg='#0069c0')
        self.save_edition.place(x = 330, y = 50)
        self.cancel = tk.Button(self.otra_ventana, text="Cancelar", command = self.otra_ventana.destroy, fg='white', bg='#0069c0')
        self.cancel.place(x = 470, y = 50)


    def save(self):
        nombre = self.nombre.get()
        titulo = self.tema.get()
        tarjeta = self.tarjeta.get("1.0", "end-1c")
        posicion = self.posicion.get("1.0", "end-1c")
        completo = self.conector.editar(self.card[0], nombre, titulo, tarjeta, posicion)
        self.otra_ventana.destroy()
        print("guarda datos")
