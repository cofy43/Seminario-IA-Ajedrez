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

class Principal():
    def __init__(self) :
        self.ventana = tk.Tk()
        self.ventana.geometry("900x690")
        self.ventana.title("Targetero")
        self.ventana['bg'] = '#26a69a'
        self.connector = Db_connector()
        self.connector.connect()

        self.nombre = tk.Label(self.ventana, text='Nombre: ', bg='#26a69a', fg="black")
        self.nombre.place(x =30, y=20)
        self.tema = tk.Label(self.ventana, text='Tema: ', bg='#26a69a', fg="black")
        self.tajeta = tk.Text(self.ventana, width=40, height=18)
        self.tajeta.place(x=30, y=150)
        self.font = tkFont.Font(family="Chess Cases", size=23)
        self.posicion = tk.Text(self.ventana, width=16, height=9.5, font=self.font)
        self.posicion.place(x=380, y=150)
        self.tema.place(x =30, y=100)
        self.t3 = tk.Frame(self.ventana)
        self.t3.place(x=100, y=480, width=570, height=190)

        self.new_card = tk.Button(self.ventana, text="Nueva tarjeta", command = self.create_card, fg='white', bg='#00766c')
        self.new_card.place(x = 750, y = 104)
        self.edit_card = tk.Button(self.ventana, text="Editar tarjeta", command = self.create_card, fg='white', bg='#00766c')
        self.edit_card.place(x = 750, y = 154)
        self.delete_card = tk.Button(self.ventana, text="Borrar tarjeta", command = self.create_card, fg='white', bg='#00766c')
        self.delete_card.place(x = 750, y = 204)
        self.search_card = tk.Button(self.ventana, text="Buscar tarjeta", command = self.create_card, fg='white', bg='#00766c')
        self.search_card.place(x = 750, y = 254)

        self.close = tk.Button(self.ventana, text="Terminar", command = self.ventana.destroy, fg='white', bg='#00766c')
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
        new_card.otra_ventana.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_closing(self):
        print("cerro nueva carta")
        self.connector.connect()
        self.crea_tabla()

    def crea_tabla(self):
        headers = (u"id", u"Nombre", u"Tarjeta", u"Tema")
        title_table = 'Número de tarjetas encontradas: {:d}'.format(len(self.list_data))
        self.tabla = Table(self.t3, title=title_table, headers=headers, list_game=self.list_data, ventana=self.ventana)
        self.tabla.pack()

        col = []
        temp = []
        for item in self.list_data:
            i = 0
            for key in item:
                if i != 3:
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
        self.tajeta.insert(tk.END, card[2])
        self.posicion.insert(tk.END, card[3])
        print(self.id_card)

if __name__ == "__main__":
    juego  = Principal()
    juego.ventana.mainloop() 