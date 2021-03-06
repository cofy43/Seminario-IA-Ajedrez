import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
from tkinter import filedialog
import tkinter.font as tkFont
import os
from PIL import ImageTk, Image
import io


from db_connector import Db_connector
from table import Table
from new_card import New_card
from edit_card import Edit_card

class Principal():
    def __init__(self) :
        self.ventana = tk.Tk()
        self.ventana.geometry("900x690")
        self.ventana.title("Targetero")
        self.ventana['bg'] = '#455a64'
        self.connector = Db_connector()
        self.connector.connect()

        self.nombre = tk.Label(self.ventana, text='Nombre: ', bg='#455a64', fg="white")
        self.nombre.place(x =30, y=20)
        self.nombre_value = tk.Label(self.ventana, text='--', bg='#455a64', fg="white")
        self.nombre_value.place(x =100, y=20)
        self.tema = tk.Label(self.ventana, text='Tema: ', bg='#455a64', fg="white")
        self.tema.place(x =30, y=100)
        self.tema_value = tk.Label(self.ventana, text='--', bg='#455a64', fg="white")
        self.tema_value.place(x =85, y=100)

        self.tajeta = tk.Text(self.ventana, width=40, height=18)
        self.tajeta.place(x=30, y=150)
        self.font = tkFont.Font(family="Chess Cases", size=23)
        self.posicion = tk.Text(self.ventana, width=16, height=9.5, font=self.font)
        self.posicion.place(x=380, y=150)
        self.t3 = tk.Frame(self.ventana)
        self.t3.place(x=100, y=480, width=570, height=190)

        self.new_card = tk.Button(self.ventana, text="Nueva tarjeta", command = self.create_card, fg='white', bg='#1c313a')
        self.new_card.place(x = 750, y = 104)
        self.edit_card = tk.Button(self.ventana, text="Editar tarjeta", command = self.edit_card, fg='white', bg='#1c313a')
        self.edit_card.place(x = 750, y = 154)
        self.delete_card = tk.Button(self.ventana, text="Borrar tarjeta", command = self.delete_card, fg='white', bg='#1c313a')
        self.delete_card.place(x = 750, y = 204)
        self.refresh_info = tk.Button(self.ventana, text="Refescar\n información", command = self.refresca_tabla, fg='white', bg='#1c313a')
        self.refresh_info.place(x = 750, y = 304)

        self.close = tk.Button(self.ventana, text="Terminar", command = self.ventana.destroy, fg='white', bg='#1c313a')
        self.close.place(x = 750, y = 554)

        self.list_data = self.connector.list_data
        print(self.list_data)
        self.id_card = -1
        self.tabla = None
        self.crea_tabla()
        self.ventana.bind("<Double-1>",self.get_id_card)
        self.limit_max = len(self.list_data)-1

    def create_card(self):
        print("boton")
        new_card = New_card(self.connector, self.ventana, len(self.list_data))
        new_card.otra_ventana.protocol("WM_DESTROY_WINDOW", self.on_closing)

    def edit_card(self):
        card = self.list_data[self.id_card]
        edit = Edit_card(self.connector, self.ventana, card)
    
    def delete_card(self):
        card = self.list_data[self.id_card]
        mensaje = ("Esta seguro de que quiere eliminar la tarjeta con Nombre: %s y Tema: %s.\n Este movimiento es irreversible.") % (card[1], card[2])
        respuesta = messagebox.askquestion(title=None, message=mensaje)
        if (respuesta == 'yes'):
            self.connector.borrar(card[0])
            self.refresca_tabla()

    def on_closing(self):
        print("cerro nueva carta")
        self.connector.connect()
        self.crea_tabla()

    def crea_tabla(self):
        headers = (u"id", u"Nombre", u"Tarjeta")
        title_table = 'Número de tarjetas encontradas: {:d}'.format(len(self.list_data))
        self.tabla = Table(self.t3, title=title_table, headers=headers, list_game=self.list_data, ventana=self.ventana)
        self.tabla.pack()

        col = []
        temp = []
        for item in self.list_data:
            i = 0
            for key in item:
                if i != 3 and i != 4:
                    temp.append(key)
                i += 1
            col.append(temp)
            temp = []

        for row in col:
            self.tabla.add_row(row)

    def get_id_card(self, event):
        self.tajeta.delete('1.0', END)
        self.posicion.delete('1.0', END)
        self.id_card = self.tabla.id_card
        self.tabla.indice = -1
        card = self.list_data[self.id_card]
        self.tajeta.insert(tk.END, card[4])
        self.posicion.insert(tk.END, card[3])
        self.nombre_value.config(text=card[1])
        self.tema_value.config(text=card[2])

    def refresca_tabla(self):
        self.connector.connect()
        self.list_data = self.connector.list_data
        self.tabla.destroy()
        self.tabla = None
        self.crea_tabla()
if __name__ == "__main__":
    juego  = Principal()
    juego.ventana.mainloop() 