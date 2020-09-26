#!/usr/bin/env python

import tkinter as tk
from PIL import ImageTk, Image
import os

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

# Definición de las piezas
alfil_blanco = ImageTk.PhotoImage(Image.open(path + "Abb.jpg"))
alfil_b = tk.Label(ventana, image = alfil_blanco )
alfil_b.pack(side = "bottom", fill = "both", expand = "yes")
alfil_b.place(x = 200, y = 100)

alfil_negro = ImageTk.PhotoImage(Image.open(path + "Anb.jpg"))
alfil_n = tk.Label(ventana, image = alfil_negro )
alfil_n.pack(side = "bottom", fill = "both", expand = "yes")
alfil_n.place(x = 200, y = 500)

caballo_blanco = ImageTk.PhotoImage(Image.open(path + "Cbb.jpg"))
caballo_b = tk.Label(ventana, image = caballo_blanco )
caballo_b.pack(side = "bottom", fill = "both", expand = "yes")
caballo_b.place(x = 250, y = 100)

caballo_negro = ImageTk.PhotoImage(Image.open(path + "Cnb.jpg"))
caballo_n = tk.Label(ventana, image = caballo_negro )
caballo_n.pack(side = "bottom", fill = "both", expand = "yes")
caballo_n.place(x = 250, y = 500)

torre_blanco = ImageTk.PhotoImage(Image.open(path + "Tbb.jpg"))
torre_b = tk.Label(ventana, image = torre_blanco )
torre_b.pack(side = "bottom", fill = "both", expand = "yes")
torre_b.place(x = 300, y = 100)

torre_negro = ImageTk.PhotoImage(Image.open(path + "Tnb.jpg"))
torre_n = tk.Label(ventana, image = torre_negro )
torre_n.pack(side = "bottom", fill = "both", expand = "yes")
torre_n.place(x = 300, y = 500)

peon_blanco = ImageTk.PhotoImage(Image.open(path + "Pbb.jpg"))
peon_b = tk.Label(ventana, image = peon_blanco )
peon_b.pack(side = "bottom", fill = "both", expand = "yes")
peon_b.place(x = 350, y = 100)

peon_negro = ImageTk.PhotoImage(Image.open(path + "Pnb.jpg"))
peon_n = tk.Label(ventana, image = peon_negro )
peon_n.pack(side = "bottom", fill = "both", expand = "yes")
peon_n.place(x = 350, y = 500)

dama_blanco = ImageTk.PhotoImage(Image.open(path + "Dbb.jpg"))
dama_b = tk.Label(ventana, image = dama_blanco )
dama_b.pack(side = "bottom", fill = "both", expand = "yes")
dama_b.place(x = 400, y = 100)

dama_negro = ImageTk.PhotoImage(Image.open(path + "Dnb.jpg"))
dama_n = tk.Label(ventana, image = dama_negro )
dama_n.pack(side = "bottom", fill = "both", expand = "yes")
dama_n.place(x = 400, y = 500)

rey_blanco = ImageTk.PhotoImage(Image.open(path + "Rbb.jpg"))
rey_b = tk.Label(ventana, image = rey_blanco )
rey_b.pack(side = "bottom", fill = "both", expand = "yes")
rey_b.place(x = 450, y = 100)

rey_negro = ImageTk.PhotoImage(Image.open(path + "Rnb.jpg"))
rey_n = tk.Label(ventana, image = rey_negro )
rey_n.pack(side = "bottom", fill = "both", expand = "yes")
rey_n.place(x = 450, y = 500)


ventana.mainloop()