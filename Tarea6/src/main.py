import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
from tkinter import filedialog
import os
from PIL import ImageTk, Image
import io


from db_connector import Db_connector
from table import Table

class Principal():
    def __init__(self) :
        self.ventana = tk.Tk()
        self.ventana.geometry("900x690")
        self.ventana.title("Targetero")
        self.ventana['bg'] = '#344266'
        self.connector = Db_connector()
        self.connector.connect()
        self.nombre = tk.Label(self.ventana, text='Nombre: ', bg='#344266', fg="white")
        self.nombre.place(x =30, y=20)
        self.tema = tk.Label(self.ventana, text='Tema: ', bg='#344266', fg="white")
        self.tajeta = tk.Text(self.ventana, width=40, height=18)
        self.tajeta.place(x=30, y=150)
        self.posicion = tk.Text(self.ventana, width=40, height=18, font=("Chess Merida", ) )
        self.posicion.place(x=400, y=150)
        self.tema.place(x =30, y=100)
        self.list_data = self.connector.list_data
        print(self.list_data)
        self.id_card = -1
        self.t3 = tk.Frame(self.ventana)
        self.t3.place(x=100, y=480, width=570, height=190)
        self.tabla = None
        self.crea_tabla()
        self.ventana.bind("<Double-1>",self.get_id_card)
        self.limit_max = len(self.list_data)-1

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
        if self.tajeta.get(tk.END) != "":
            self.tajeta.delete(0,tk.END)
        if self.posicion.get(tk.END) != "":
            self.posicion.delete(0,tk.END)
        self.id_card = self.tabla.id_card
        self.tabla.indice = -1
        card = self.list_data[self.id_card]
        self.tajeta.insert(tk.END, card[2])
        self.posicion.insert(tk.END, card[3])
        print(self.id_card)

if __name__ == "__main__":
    juego  = Principal()
    juego.ventana.mainloop() 