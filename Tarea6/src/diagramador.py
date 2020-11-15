#!/usr/bin/env python

import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import filedialog
from tablero import Tablero
#from fonts import Fonst
import os
import io

class Diagramador(tk.Frame):
    def __init__(self, ventana, posicion):

        self.path = "piezas-ajedrez/"
        self.posicion = posicion
        # Definición de self.ventana
        self.ventana = tk.Toplevel(ventana)
        self.ventana.geometry("650x600")
        self.ventana.title("Diagrama de Ajedrez")
        self.tablero = Tablero(self.ventana)

        self.boton2 = tk.Button(self.ventana, text="Agregar posición", command = self.salvar_partida)
        self.boton2.pack()
        self.boton2.place(x=130, y=10)

        self.boton3 = tk.Button(self.ventana, text="Limpiar posición", command = self.nueva_partida)
        self.boton3.pack()
        self.boton3.place(x=260, y=10)

        self.button = tk.Button(self.ventana ,text = "Cerrar", command = self.close_window)
        self.button.pack()
        self.button.place(x=540, y=10)

        alfil_blanco = ImageTk.PhotoImage(Image.open(self.path + "Abb.jpg"))
        self.alfil_b = tk.Button(self.ventana, image = alfil_blanco, command = lambda: self.setPiece("Ab"))
        self.alfil_b.pack()
        self.alfil_b.place(x = 70, y = 480)

        alfil_negro = ImageTk.PhotoImage(Image.open(self.path + "Anb.jpg"))
        self.alfil_n = tk.Button(self.ventana, image = alfil_negro, command = lambda: self.setPiece("An"))
        self.alfil_n.pack()
        self.alfil_n.place(x = 70, y = 80)

        caballo_blanco = ImageTk.PhotoImage(Image.open(self.path + "Cbb.jpg"))
        self.caballo_b = tk.Button(self.ventana, image = caballo_blanco, command = lambda: self.setPiece("Cb"))
        self.caballo_b.pack()
        self.caballo_b.place(x = 120, y = 480)

        caballo_negro = ImageTk.PhotoImage(Image.open(self.path + "Cnb.jpg"))
        self.caballo_n = tk.Button(self.ventana, image = caballo_negro, command = lambda: self.setPiece("Cn"))
        self.caballo_n.pack()
        self.caballo_n.place(x = 120, y = 80)

        torre_blanco = ImageTk.PhotoImage(Image.open(self.path + "Tbb.jpg"))
        self.torre_b = tk.Button(self.ventana, image = torre_blanco, command = lambda: self.setPiece("Tb"))
        self.torre_b.pack()
        self.torre_b.place(x = 170, y = 480)

        torre_negro = ImageTk.PhotoImage(Image.open(self.path + "Tnb.jpg"))
        self.torre_n = tk.Button(self.ventana, image = torre_negro, command = lambda: self.setPiece("Tn"))
        self.torre_n.pack()
        self.torre_n.place(x = 170, y = 80)

        peon_blanco = ImageTk.PhotoImage(Image.open(self.path + "Pbb.jpg"))
        self.peon_b = tk.Button(self.ventana, image = peon_blanco, command = lambda: self.setPiece("Pb"))
        self.peon_b.pack()
        self.peon_b.place(x = 220, y = 480)

        peon_negro = ImageTk.PhotoImage(Image.open(self.path + "Pnb.jpg"))
        self.peon_n = tk.Button(self.ventana, image = peon_negro, command = lambda: self.setPiece("Pn"))
        self.peon_n.pack()
        self.peon_n.place(x = 220, y = 80)

        dama_blanco = ImageTk.PhotoImage(Image.open(self.path + "Dbb.jpg"))
        self.dama_b = tk.Button(self.ventana, image = dama_blanco, command = lambda: self.setPiece("Db"))
        self.dama_b.pack()
        self.dama_b.place(x = 270, y = 480)

        dama_negro = ImageTk.PhotoImage(Image.open(self.path + "Dnb.jpg"))
        self.dama_n = tk.Button(self.ventana, image = dama_negro, command = lambda: self.setPiece("Dn"))
        self.dama_n.pack()
        self.dama_n.place(x = 270, y = 80)

        rey_blanco = ImageTk.PhotoImage(Image.open(self.path + "Rbb.jpg"))
        self.rey_b = tk.Button(self.ventana, image = rey_blanco, command = lambda: self.setPiece("Rb"))
        self.rey_b.pack()
        self.rey_b.place(x = 320, y = 480)

        rey_negro = ImageTk.PhotoImage(Image.open(self.path + "Rnb.jpg"))
        self.rey_n = tk.Button(self.ventana, image = rey_negro, command = lambda: self.setPiece("Rn"))
        self.rey_n.pack()
        self.rey_n.place(x = 320, y = 80)

        delete_pice_back = ImageTk.PhotoImage(Image.open(self.path + "trash.jpg"))
        self.delete_pb = tk.Button(self.ventana, image = delete_pice_back, command = lambda: self.setPiece("trash"))
        self.delete_pb.pack()
        self.delete_pb.place(x = 370, y = 80)

        delete_pice_white = ImageTk.PhotoImage(Image.open(self.path + "trash.jpg"))
        self.delete_pw = tk.Button(self.ventana, image = delete_pice_white, command = lambda: self.setPiece("trash"))
        self.delete_pw.pack()
        self.delete_pw.place(x = 370, y = 480)

        self.tablero.pack()
        self.tablero.place(x=70, y = 142)

    def setPiece(self, pice):
        self.tablero.setPiece(pice)

    def salvar_partida(self):
        self.merida_pieces = {"Tbb.jpg" : "r", "Tbn.jpg" : "R", "Tnb.jpg" : "t", "Tnn.jpg" : "T",
                              "Cbb.jpg" : "n", "Cbn.jpg" : "N", "Cnb.jpg" : "m", "Cnn.jpg" : "M",
                              "Abb.jpg" : "b", "Abn.jpg" : "B", "Anb.jpg" : "v", "Ann.jpg" : "V",
                              "Dbb.jpg" : "q", "Dbn.jpg" : "Q", "Dnb.jpg" : "w", "Dnn.jpg" : "W",
                              "Rbb.jpg" : "k", "Rbn.jpg" : "K", "Rnb.jpg" : "l", "Rnn.jpg" : "L",
                              "Pbb.jpg" : "p", "Pbn.jpg" : "P", "Pnb.jpg" : "o", "Pnn.jpg" : "O",
                              "b.jpg" : " ", "n.jpg" : "+", "9" : "!\"\"\"\"\"\"\"\"#", 
                              "0" : "/(((((((()"}
        self.vertilcal_inicial = "$"
        self.vertilcal_final = "%"
        board = self.tablero.getTablero()
        posicion = ''
        posicion = self.merida_pieces["9"] + '\n'
        for r in range(8):
            row = self.vertilcal_inicial
            for c in range(8):
                piece = board[r][c]
                row = row + self.merida_pieces[piece]
            row = row + self.vertilcal_final + '\n'
            posicion += row 
        posicion += self.merida_pieces["0"]
        self.posicion.delete('1.0', tk.END)
        self.posicion.insert(tk.END, posicion)
        self.close_window()

    def close_window(self):
        self.ventana.destroy()


    def nueva_partida(self):
        self.tablero.fill_board()