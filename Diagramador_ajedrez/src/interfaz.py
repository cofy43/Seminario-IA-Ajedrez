#!/usr/bin/env python

import tkinter as tk
from PIL import ImageTk, Image
from tkinter import filedialog
from tablero import Tablero
from fonts import Fonst
import os
import io

path = "piezas-ajedrez/"

OptionList = [
"Chess Assistant",
"Tilburg",
"TascBase",
"ChessBase",
"Cheq True Type",
"Marroquin"
]

# Definición de ventana
ventana = tk.Tk()

ventana.geometry("800x600")
ventana.title("Diagrama de Ajedrez")
tablero = Tablero(ventana)
fonts = Fonst()

#  Funciones para los botones

def leer_partida():
    print("Aqui va el codigo para cargar archivo")
    path = filedialog.askopenfilename(title="Abrir partida", initialdir="./", filetypes=[("Text files","*.txt")])
    board = fonts.lee(path)
    tablero.setTablero(board)

def salvar_partida():
    board = tablero.getTablero()
    #archivo = filediaglog.sksaveasfilename(title = "Guardar partida", defaultextension=".txt")
    paht = filedialog.asksaveasfilename(title = "Guardar partida", defaultextension=".txt", filetypes=[("Text files","*.txt")])
    fonts.guarda(board, paht)

def nueva_partida():
    tablero.fill_board()

def capturar_imagen():
    print("Aqui va el codigo para capturar imagen")
    ps = tablero.el_tablero.postscript(colormode='color')
    img = Image.open(io.BytesIO(ps.encode('utf-8') ))
    paht = filedialog.asksaveasfilename(title = "Guardar partida", defaultextension=".jpg", filetypes=[("Images files","*.jpg")])
    img.save(paht, 'jpeg')



def diagrama_html():
    print("Aqui va el codigo para diagrama html")


# Definiciones de botones

boton1 = tk.Button(ventana, text="Leer partida", command = leer_partida)
boton1.pack()
boton1.place(x=10, y=10)

boton2 = tk.Button(ventana, text="Salvar partida", command = salvar_partida)
boton2.pack()
boton2.place(x=150, y=10)

tipografias = tk.StringVar(ventana)
tipografias.set(OptionList[0])

opciones = tk.OptionMenu(ventana, tipografias, *OptionList)
opciones.config(font=('Helvetica', 12))
opciones.pack()
opciones.place(x=305, y=10)

boton3 = tk.Button(ventana, text="Nueva partida", command = nueva_partida)
boton3.pack()
boton3.place(x=500, y=10)

boton5 = tk.Button(ventana, text="Capturar imagen", command = capturar_imagen)
boton5.pack()
boton5.place(x=650, y=10)

boton6 = tk.Button(ventana, text="Diagrama html", command = diagrama_html)
boton6.pack()
boton6.place(x=250, y=60)

button = tk.Button(ventana ,text = "Cerrar", command = ventana.destroy)
button.pack()
button.place(x=400, y=60)

def setPiece(pice):
    print("--- " + pice)
    tablero.setPiece(pice)


# Definición de las piezas
alfil_blanco = ImageTk.PhotoImage(Image.open(path + "Abb.jpg"))
alfil_b = tk.Button(ventana, image = alfil_blanco, command = lambda: setPiece("Ab"))
alfil_b.pack()
alfil_b.place(x = 200, y = 500)

alfil_negro = ImageTk.PhotoImage(Image.open(path + "Anb.jpg"))
alfil_n = tk.Button(ventana, image = alfil_negro, command = lambda: setPiece("An"))
alfil_n.pack()
alfil_n.place(x = 200, y = 100)

caballo_blanco = ImageTk.PhotoImage(Image.open(path + "Cbb.jpg"))
caballo_b = tk.Button(ventana, image = caballo_blanco, command = lambda: setPiece("Cb"))
caballo_b.pack()
caballo_b.place(x = 250, y = 500)

caballo_negro = ImageTk.PhotoImage(Image.open(path + "Cnb.jpg"))
caballo_n = tk.Button(ventana, image = caballo_negro, command = lambda: setPiece("Cn"))
caballo_n.pack()
caballo_n.place(x = 250, y = 100)

torre_blanco = ImageTk.PhotoImage(Image.open(path + "Tbb.jpg"))
torre_b = tk.Button(ventana, image = torre_blanco, command = lambda: setPiece("Tb"))
torre_b.pack()
torre_b.place(x = 300, y = 500)

torre_negro = ImageTk.PhotoImage(Image.open(path + "Tnb.jpg"))
torre_n = tk.Button(ventana, image = torre_negro, command = lambda: setPiece("Tn"))
torre_n.pack()
torre_n.place(x = 300, y = 100)

peon_blanco = ImageTk.PhotoImage(Image.open(path + "Pbb.jpg"))
peon_b = tk.Button(ventana, image = peon_blanco, command = lambda: setPiece("Pb"))
peon_b.pack()
peon_b.place(x = 350, y = 500)

peon_negro = ImageTk.PhotoImage(Image.open(path + "Pnb.jpg"))
peon_n = tk.Button(ventana, image = peon_negro, command = lambda: setPiece("Pn"))
peon_n.pack()
peon_n.place(x = 350, y = 100)

dama_blanco = ImageTk.PhotoImage(Image.open(path + "Dbb.jpg"))
dama_b = tk.Button(ventana, image = dama_blanco, command = lambda: setPiece("Db"))
dama_b.pack()
dama_b.place(x = 400, y = 500)

dama_negro = ImageTk.PhotoImage(Image.open(path + "Dnb.jpg"))
dama_n = tk.Button(ventana, image = dama_negro, command = lambda: setPiece("Dn"))
dama_n.pack()
dama_n.place(x = 400, y = 100)

rey_blanco = ImageTk.PhotoImage(Image.open(path + "Rbb.jpg"))
rey_b = tk.Button(ventana, image = rey_blanco, command = lambda: setPiece("Rb"))
rey_b.pack()
rey_b.place(x = 450, y = 500)

rey_negro = ImageTk.PhotoImage(Image.open(path + "Rnb.jpg"))
rey_n = tk.Button(ventana, image = rey_negro, command = lambda: setPiece("Rn"))
rey_n.pack()
rey_n.place(x = 450, y = 100)

tablero.pack()

ventana.mainloop()