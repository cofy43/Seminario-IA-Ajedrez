import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import *
from tkinter import filedialog


from parser import Parser
from table import Table
from game import Game
from tablero import Tablero


class Principal():
    def __init__(self) :
        self.ventana = tk.Tk()
        self.ventana.geometry("650x600")
        self.ventana.title("Lector de partidas PGN")
        self.parser = None
        self.partidas_completas = []
        self.list_game = []
        self.tabla = None
        self.crea_ventana()

    def crea_ventana(self):
        label = Label(self.ventana,text="!Bienvenido¡\n Por favor elige un archivo PGN para comenzar")
        label.place(x=280, y=20)
        label.pack()   
        boton1 = tk.Button(self.ventana, text="Leer partida", command = self.leer_partida)
        boton1.pack()
        boton1.place(x=280, y=80)

    def leer_partida(self):
        self.tabla = None
        self.list_game = []
        try:
            path = filedialog.askopenfilename(title="Abrir partida", initialdir="./", filetypes=[("Text files","*.pgn"), ("All file", "*.*")])
            self.parser = Parser(path)
            for item in self.parser.games:
                game = Game(item)
                self.list_game.append(game)
            self.crea_tabla()
        except FileNotFoundError as e:
            messagebox.showerror(title="ERROR", message="No se encontró el archivo, por favor validalo e intentalo de nuevo")
        except TypeError as e:
            messagebox.showerror(title="ERROR", message="El formato del archivo no es válido o no se seleccionó uno, por favor validalo e intentalo de nuevo")

    def crea_tabla(self):
        t3 = tk.Frame(self.ventana)
        t3.place(x=0, y=150, width=650, height=600 )

        headers = (u"Event",   u"Site", u"Date", u"Round", u"White",   u"Black", u"Result" )

        title_table = 'Número de partidas encontradas: {:d}'.format(self.parser.n_games)
        self.tabla = Table(t3, title=title_table, headers=headers, list_game=self.list_game, ventana=self.ventana)
        self.tabla.pack()

        cursor = []
        temp = []
        for item in self.list_game:
            for key in headers:
                temp.append(item.header[key.lower()])
            cursor.append(temp)
            temp = []

        for row in cursor:   
            self.tabla.add_row(row)

if __name__ == "__main__":
    juego  = Principal()
    juego.ventana.mainloop() 
    pass