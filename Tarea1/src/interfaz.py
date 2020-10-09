#!/usr/bin/env python

import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import filedialog
from tablero import Tablero
from fonts import Fonst
import os
import io

path = "piezas-ajedrez/"
# Definición de ventana
ventana = tk.Tk()
ventana.geometry("650x600")
ventana.title("Diagrama de Ajedrez")
tablero = Tablero(ventana)
fonts = Fonst()

#  Funciones para los botones

def leer_partida():
    path = filedialog.askopenfilename(title="Abrir partida", initialdir="./", filetypes=[("Text files","*.txt")])
    board = fonts.lee(path)
    if (not bool(board)) :
        messagebox.showerror(title="ERROR", message="El formato del archivo no es válido, por favor validalo e intentalo de nuevo")
    else: 
        tablero.setTablero(board)


def salvar_partida():
    board = tablero.getTablero()
    paht = filedialog.asksaveasfilename(title = "Guardar partida", defaultextension=".txt", filetypes=[("Text files","*.txt")])
    fonts.guarda(board, paht)

def nueva_partida():
    tablero.fill_board()

def capturar_imagen():
    ps = tablero.el_tablero.postscript(colormode='color')
    img = Image.open(io.BytesIO(ps.encode('utf-8') ))
    paht = filedialog.asksaveasfilename(title = "Guardar partida", defaultextension=".jpg", filetypes=[("Images files","*.jpg")])
    img.save(paht, 'jpeg')


# Definiciones de botones

boton1 = tk.Button(ventana, text="Leer partida", command = leer_partida)
boton1.pack()
boton1.place(x=10, y=10)

boton2 = tk.Button(ventana, text="Salvar partida", command = salvar_partida)
boton2.pack()
boton2.place(x=130, y=10)

boton3 = tk.Button(ventana, text="Nueva partida", command = nueva_partida)
boton3.pack()
boton3.place(x=260, y=10)

boton5 = tk.Button(ventana, text="Capturar imagen", command = capturar_imagen)
boton5.pack()
boton5.place(x=390, y=10)

button = tk.Button(ventana ,text = "Cerrar", command = ventana.destroy)
button.pack()
button.place(x=540, y=10)

def setPiece(pice):
    tablero.setPiece(pice)

# Definición de las piezas
alfil_blanco = ImageTk.PhotoImage(Image.open(path + "Abb.jpg"))
alfil_b = tk.Button(ventana, image = alfil_blanco, command = lambda: setPiece("Ab"))
alfil_b.pack()
alfil_b.place(x = 70, y = 480)

alfil_negro = ImageTk.PhotoImage(Image.open(path + "Anb.jpg"))
alfil_n = tk.Button(ventana, image = alfil_negro, command = lambda: setPiece("An"))
alfil_n.pack()
alfil_n.place(x = 70, y = 80)

caballo_blanco = ImageTk.PhotoImage(Image.open(path + "Cbb.jpg"))
caballo_b = tk.Button(ventana, image = caballo_blanco, command = lambda: setPiece("Cb"))
caballo_b.pack()
caballo_b.place(x = 120, y = 480)

caballo_negro = ImageTk.PhotoImage(Image.open(path + "Cnb.jpg"))
caballo_n = tk.Button(ventana, image = caballo_negro, command = lambda: setPiece("Cn"))
caballo_n.pack()
caballo_n.place(x = 120, y = 80)

torre_blanco = ImageTk.PhotoImage(Image.open(path + "Tbb.jpg"))
torre_b = tk.Button(ventana, image = torre_blanco, command = lambda: setPiece("Tb"))
torre_b.pack()
torre_b.place(x = 170, y = 480)

torre_negro = ImageTk.PhotoImage(Image.open(path + "Tnb.jpg"))
torre_n = tk.Button(ventana, image = torre_negro, command = lambda: setPiece("Tn"))
torre_n.pack()
torre_n.place(x = 170, y = 80)

peon_blanco = ImageTk.PhotoImage(Image.open(path + "Pbb.jpg"))
peon_b = tk.Button(ventana, image = peon_blanco, command = lambda: setPiece("Pb"))
peon_b.pack()
peon_b.place(x = 220, y = 480)

peon_negro = ImageTk.PhotoImage(Image.open(path + "Pnb.jpg"))
peon_n = tk.Button(ventana, image = peon_negro, command = lambda: setPiece("Pn"))
peon_n.pack()
peon_n.place(x = 220, y = 80)

dama_blanco = ImageTk.PhotoImage(Image.open(path + "Dbb.jpg"))
dama_b = tk.Button(ventana, image = dama_blanco, command = lambda: setPiece("Db"))
dama_b.pack()
dama_b.place(x = 270, y = 480)

dama_negro = ImageTk.PhotoImage(Image.open(path + "Dnb.jpg"))
dama_n = tk.Button(ventana, image = dama_negro, command = lambda: setPiece("Dn"))
dama_n.pack()
dama_n.place(x = 270, y = 80)

rey_blanco = ImageTk.PhotoImage(Image.open(path + "Rbb.jpg"))
rey_b = tk.Button(ventana, image = rey_blanco, command = lambda: setPiece("Rb"))
rey_b.pack()
rey_b.place(x = 320, y = 480)

rey_negro = ImageTk.PhotoImage(Image.open(path + "Rnb.jpg"))
rey_n = tk.Button(ventana, image = rey_negro, command = lambda: setPiece("Rn"))
rey_n.pack()
rey_n.place(x = 320, y = 80)

delete_pice_back = ImageTk.PhotoImage(Image.open(path + "trash.jpg"))
delete_pb = tk.Button(ventana, image = delete_pice_back, command = lambda: setPiece("trash"))
delete_pb.pack()
delete_pb.place(x = 370, y = 80)

delete_pice_white = ImageTk.PhotoImage(Image.open(path + "trash.jpg"))
delete_pw = tk.Button(ventana, image = delete_pice_white, command = lambda: setPiece("trash"))
delete_pw.pack()
delete_pw.place(x = 370, y = 480)

tablero.pack()
tablero.place(x=70, y = 142)

ventana.mainloop()