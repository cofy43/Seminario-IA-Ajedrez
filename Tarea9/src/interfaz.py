#!/usr/bin/env python

import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import filedialog
from tablero import Tablero
import os
import io

class Diagramador(tk.Frame):
    def __init__(self, ventana, is_answer):
        # Definición de ventana
        self.path = "piezas-ajedrez/"
        self.ventana = tk.Toplevel(ventana)
        self.game = tk.Frame(self.ventana)

        if not(is_answer):
            self.ventana.geometry("520x480")
            self.ventana.title("Diagrama de Ajedrez")
            self.ventana['bg'] = '#ffffa8'
            self.boton3 = tk.Button(self.ventana, text="Limpiar tablero", command = self.nueva_partida, fg='black', bg='#cabf45')
            self.boton3.pack()
            self.boton3.place(x=370, y=200)
            self.button = tk.Button(self.ventana ,text = "Salvar posicion", command = self.ventana.destroy, fg='black', bg='#cabf45')
            self.button.pack()
            self.button.place(x=370, y=240)
            self.alfil_blanco = ImageTk.PhotoImage(Image.open(self.path + "Abb.jpg"))
            self.alfil_b = tk.Button(self.ventana, image = self.alfil_blanco, command = lambda: self.setPiece("Ab"), fg='black', bg='#cabf45')
            self.alfil_b.pack()
            self.alfil_b.place(x = 20, y = 410)

            self.alfil_negro = ImageTk.PhotoImage(Image.open(self.path + "Anb.jpg"))
            self.alfil_n = tk.Button(self.ventana, image = self.alfil_negro, command = lambda: self.setPiece("An"), fg='black', bg='#cabf45')
            self.alfil_n.pack()
            self.alfil_n.place(x = 20, y = 10)

            self.caballo_blanco = ImageTk.PhotoImage(Image.open(self.path + "Cbb.jpg"))
            self.caballo_b = tk.Button(self.ventana, image = self.caballo_blanco, command = lambda: self.setPiece("Cb"), fg='black', bg='#cabf45')
            self.caballo_b.pack()
            self.caballo_b.place(x = 70, y = 410)

            self.caballo_negro = ImageTk.PhotoImage(Image.open(self.path + "Cnb.jpg"))
            self.caballo_n = tk.Button(self.ventana, image = self.caballo_negro, command = lambda: self.setPiece("Cn"), fg='black', bg='#cabf45')
            self.caballo_n.pack()
            self.caballo_n.place(x = 70, y = 10)

            self.torre_blanco = ImageTk.PhotoImage(Image.open(self.path + "Tbb.jpg"))
            self.torre_b = tk.Button(self.ventana, image = self.torre_blanco, command = lambda: self.setPiece("Tb"), fg='black', bg='#cabf45')
            self.torre_b.pack()
            self.torre_b.place(x = 120, y = 410)

            self.torre_negro = ImageTk.PhotoImage(Image.open(self.path + "Tnb.jpg"))
            self.torre_n = tk.Button(self.ventana, image = self.torre_negro, command = lambda: self.setPiece("Tn"), fg='black', bg='#cabf45')
            self.torre_n.pack()
            self.torre_n.place(x = 120, y = 10)

            self.peon_blanco = ImageTk.PhotoImage(Image.open(self.path + "Pbb.jpg"))
            self.peon_b = tk.Button(self.ventana, image = self.peon_blanco, command = lambda: self.setPiece("Pb"), fg='black', bg='#cabf45')
            self.peon_b.pack()
            self.peon_b.place(x = 170, y = 410)

            self.peon_negro = ImageTk.PhotoImage(Image.open(self.path + "Pnb.jpg"))
            self.peon_n = tk.Button(self.ventana, image = self.peon_negro, command = lambda: self.setPiece("Pn"), fg='black', bg='#cabf45')
            self.peon_n.pack()
            self.peon_n.place(x = 170, y = 10)

            self.dama_blanco = ImageTk.PhotoImage(Image.open(self.path + "Dbb.jpg"))
            self.dama_b = tk.Button(self.ventana, image = self.dama_blanco, command = lambda: self.setPiece("Db"), fg='black', bg='#cabf45')
            self.dama_b.pack()
            self.dama_b.place(x = 220, y = 410)

            self.dama_negro = ImageTk.PhotoImage(Image.open(self.path + "Dnb.jpg"))
            self.dama_n = tk.Button(self.ventana, image = self.dama_negro, command = lambda: self.setPiece("Dn"), fg='black', bg='#cabf45')
            self.dama_n.pack()
            self.dama_n.place(x = 220, y = 10)

            self.rey_blanco = ImageTk.PhotoImage(Image.open(self.path + "Rbb.jpg")) 
            self.rey_b = tk.Button(self.ventana, image = self.rey_blanco, command = lambda: self.setPiece("Rb"), fg='black', bg='#cabf45')
            self.rey_b.pack()
            self.rey_b.place(x = 270, y = 410)

            self.rey_negro = ImageTk.PhotoImage(Image.open(self.path + "Rnb.jpg"))
            self.rey_n = tk.Button(self.ventana, image = self.rey_negro, command = lambda: self.setPiece("Rn"), fg='black', bg='#cabf45')
            self.rey_n.pack()
            self.rey_n.place(x = 270, y = 10)

            self.delete_pice_back = ImageTk.PhotoImage(Image.open(self.path + "trash.jpg"))
            self.delete_pb = tk.Button(self.ventana, image = self.delete_pice_back, command = lambda: self.setPiece("trash"), fg='black', bg='#cabf45')
            self.delete_pb.pack()
            self.delete_pb.place(x = 320, y = 10)

            self.delete_pice_white = ImageTk.PhotoImage(Image.open(self.path + "trash.jpg"))
            self.delete_pw = tk.Button(self.ventana, image = self.delete_pice_white, command = lambda: self.setPiece("trash"), fg='black', bg='#cabf45')
            self.delete_pw.pack()
            self.delete_pw.place(x = 320, y = 410)
            #142 - > 480
            #72 
            self.game.place(x=20, y = 72, width=320, height=320)
        else:
            self.ventana.geometry("320x320")
            self.ventana.title("Resultado")
            self.game.place(x=0, y = 0, width=320, height=320)

        self.tablero = Tablero(self.game, True)
        self.tablero.pack()
    def nueva_partida(self):
        self.tablero.fill_board()

    def setPiece(self, pice):
        self.tablero.setPiece(pice)

    def get_fen(self):
        return self.tablero.get_fen()