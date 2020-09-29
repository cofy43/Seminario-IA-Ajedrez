#!/usr/bin/env python

import tkinter as tk
from PIL import ImageTk, Image
import os

from tablero import Tablero

path = "../piezas-ajedrez/"

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

#  Funciones para los botones

def leer_partida():
    print("Aqui va el codigo para cargar archivo")

def salvar_partida():
    print("Aqui va el codigo para salvar archivo")

def nueva_partida():
    print("Aqui va el codigo para crear una nueva partida")

def capturar_imagen():
    print("Aqui va el codigo para capturar imagen")

def diagrama_html():
    print("Aqui va el codigo para diagrama html")


tablero = Tablero(ventana)

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
    tablero.setPiece(pice)

# Definición de las piezas
alfil_blanco = ImageTk.PhotoImage(Image.open(path + "Abb.jpg"))
alfil_b = tk.Button(ventana, image = alfil_blanco, command = setPiece("Abb.jpg"))
alfil_b.pack()
alfil_b.place(x = 200, y = 500)

alfil_negro = ImageTk.PhotoImage(Image.open(path + "Anb.jpg"))
alfil_n = tk.Button(ventana, image = alfil_negro, command = setPiece("Anb.jpg"))
alfil_n.pack()
alfil_n.place(x = 200, y = 100)

caballo_blanco = ImageTk.PhotoImage(Image.open(path + "Cbb.jpg"))
caballo_b = tk.Button(ventana, image = caballo_blanco, command = setPiece("Cbb.jpg"))
caballo_b.pack()
caballo_b.place(x = 250, y = 500)

caballo_negro = ImageTk.PhotoImage(Image.open(path + "Cnb.jpg"))
caballo_n = tk.Button(ventana, image = caballo_negro, command = setPiece("Cnb.jpg"))
caballo_n.pack()
caballo_n.place(x = 250, y = 100)

torre_blanco = ImageTk.PhotoImage(Image.open(path + "Tbb.jpg"))
torre_b = tk.Button(ventana, image = torre_blanco, command = setPiece("Tbb.jpg"))
torre_b.pack()
torre_b.place(x = 300, y = 500)

torre_negro = ImageTk.PhotoImage(Image.open(path + "Tnb.jpg"))
torre_n = tk.Button(ventana, image = torre_negro, command = tablero.setPiece("Tnb.jpg"))
torre_n.pack()
torre_n.place(x = 300, y = 100)

peon_blanco = ImageTk.PhotoImage(Image.open(path + "Pbb.jpg"))
peon_b = tk.Button(ventana, image = peon_blanco, command = tablero.setPiece("Pbb.jpg"))
peon_b.pack()
peon_b.place(x = 350, y = 500)

peon_negro = ImageTk.PhotoImage(Image.open(path + "Pnb.jpg"))
peon_n = tk.Button(ventana, image = peon_negro, command = tablero.setPiece("Pnb.jpg"))
peon_n.pack()
peon_n.place(x = 350, y = 100)

dama_blanco = ImageTk.PhotoImage(Image.open(path + "Dbb.jpg"))
dama_b = tk.Button(ventana, image = dama_blanco, command = tablero.setPiece("Dbb.jpg"))
dama_b.pack()
dama_b.place(x = 400, y = 500)

dama_negro = ImageTk.PhotoImage(Image.open(path + "Dnb.jpg"))
dama_n = tk.Button(ventana, image = dama_negro, command = tablero.setPiece("Dnb.jpg"))
dama_n.pack()
dama_n.place(x = 400, y = 100)

rey_blanco = ImageTk.PhotoImage(Image.open(path + "Rbb.jpg"))
rey_b = tk.Button(ventana, image = rey_blanco, command = tablero.setPiece("Rbb.jpg"))
rey_b.pack()
rey_b.place(x = 450, y = 500)

rey_negro = ImageTk.PhotoImage(Image.open(path + "Rnb.jpg"))
rey_n = tk.Button(ventana, image = rey_negro, command = tablero.setPiece("Rnb.jpg"))
rey_n.pack()
rey_n.place(x = 450, y = 100)

tablero.pack()

ventana.mainloop()