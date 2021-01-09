import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog

import tkinter.font as tkFont
import os
from PIL import ImageTk, Image
import io
from interfaz import Diagramador

from parser import Parser
from game import Game
from tablero import Tablero
import pgn_parser
from FEN_parser.fen_notation import Fen_notation

class Principal():
    def __init__(self) :
        self.ventana = tk.Tk()
        self.ventana.geometry("800x660")
        self.ventana.title("Ajedrez a ciegas")
        self.ventana['bg'] = '#ffffa8'
        self.FEN_parser = Fen_notation()
        self.fen_notation = ''
        self.diagramador = None
        self.num_jugada = 0
        self.hiden = True
        self.game = tk.Frame(self.ventana)
        self.game.place(x=30, y=30, width=320, height=320)
        self.board = Tablero(self.game, False)
        self.board.pack()
        self.game2 = tk.Frame(self.ventana)
        self.board2 = Tablero(self.game2, False)
        self.board2.pack()
        self.font = tkFont.Font(family="Chess Cases", size=23)
        self.position = tk.Listbox(self.ventana, width=18, height=20, selectbackground="#fff176", selectforeground="black")
        self.position.bind('<Double-Button>', self.ListOnDoubleClick)
        self.position.place(x=380, y=30)
        self.t3 = tk.Frame(self.ventana)
        self.t3.place(x=30, y=450, width=750, height=190)
        self.next = tk.Button(self.ventana, text="<", command = lambda:self.move(False), fg='black', bg='#cabf45')
        self.next.place(x = 125, y = 375)
        self.prev = tk.Button(self.ventana, text=">", command = lambda:self.move(True), fg='black', bg='#cabf45')
        self.prev.place(x = 185, y = 375)
        self.ini = tk.Button(self.ventana, text=">>|", command = lambda:self.last_move(True), fg='black', bg='#cabf45')
        self.ini.place(x = 250, y = 375)
        self.end = tk.Button(self.ventana, text="|<<", command = lambda:self.last_move(False), fg='black', bg='#cabf45')
        self.end.place(x = 55, y = 375)
        self.moves = []
        self.read_game = tk.Button(self.ventana, text="Leer partida", command = self.leer_partida, fg='black', bg='#cabf45')
        self.read_game.place(x = 550, y = 50)
        self.move_pieces = tk.Button(self.ventana, text="Poner / quitar las piezas", command = self.pieces_action, fg='black', bg='#cabf45')
        self.move_pieces.place(x = 550, y = 100)
        self.set_position = tk.Button(self.ventana, text="Colocar posición", command = self.set_p, fg='black', bg='#cabf45')
        self.set_position.place(x = 550, y = 150)
        self.compare = tk.Button(self.ventana, text="Comparar diagramas", command = self.get_diff, fg='black', bg='#cabf45')
        self.compare.place(x = 550, y = 200)
        self.close = tk.Button(self.ventana, text="Terminar", command = self.ventana.destroy, fg='black', bg='#cabf45')
        self.close.place(x = 550, y = 250)
        self.list_game = None
        self.tabla = None
        self.parser = None

        #Tabla#
        estilo = ttk.Style()
        estilo.configure("mystyle.Treeview", highlightthickness=0,
                        bd=0, background='#fff176', font=('Lucida Console', 9))
        self._headers = (u"Event",   u"Site", u"Date", u"Round", u"White",   u"Black", u"Result" )
        self._tree = ttk.Treeview(self.t3,
                                  height=190,
                                  columns=self._headers, 
                                  show="headings",
                                  style="mystyle.Treeview")
        self.num_jugada = -1
        vsb = ttk.Scrollbar(self.t3, orient="vertical", command=self._tree.yview)
        vsb.pack(side='right', fill='y')
        hsb = ttk.Scrollbar(self.t3, orient="horizontal", command=self._tree.xview)
        hsb.pack(side='bottom', fill='x')
        self._tree.configure(xscrollcommand=hsb.set, yscrollcommand=vsb.set)
        self._tree.pack(side="left")
        for header in self._headers:
            self._tree.heading(header, text=header.title())
            self._tree.column(header, stretch=True,
                              width=105)
                              #width=tkFont.Font().measure(header.title()))

        self._tree.bind("<Double-1>",self.OnDoubleClick)
        style = ttk.Style()
        style.configure("Treeview",
                        background="#cabf45",
                        foreground="black",
                        rowheight=25,
                        fieldbackground="#cabf45")
        style.map('Treeview', background=[('selected', '#cabf45')])
        self.indice = 0

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
        self._tree.delete(*self._tree.get_children())
        cursor = []
        temp = []
        for item in self.list_game:
            for key in self._headers:
                temp.append(item.header[key.lower()])
            cursor.append(temp)
            temp = []
        
        rows = len(cursor)
        step = 100 / rows
        progress = 0
        progress_bar = Progressbar(self.ventana, orient = HORIZONTAL, length = 100, mode = 'determinate', style="blue.Horizontal.TProgressbar",) 
        progress_bar["value"] = progress
        label = tk.Label(self.ventana, text="Cargando partidas")
        label.place(relx=0.50, rely=0.45, anchor=tk.CENTER)
        progress_bar.place(relx=0.5, rely=0.5, relwidth=0.80,  anchor=tk.CENTER)

        for row in cursor:   
            if not(None in row):
                self.add_row(row)
                self.ventana.update_idletasks()
                progress += step
                progress_bar["value"] = progress
        progress_bar.destroy()
        label.destroy()
        self.ventana.update_idletasks()

    def pieces_action(self):
        if self.hiden:
            self.game.pack_forget()
            self.game.pack()
            self.game2.place(x=30, y=30, width=320, height=320)
            self.hiden = False
        else:
            self.game.place(x=30, y=30, width=320, height=320)
            self.game2.pack_forget()
            self.game2.pack()
            self.hiden = True
        
    
    def set_p(self):
        self.diagramador = Diagramador(self.ventana, False)
        while self.diagramador.ventana.wait_window() != None:
            continue
        self.on_closing()

    def on_closing(self):
        self.fen_notation = self.diagramador.get_fen()

    def get_diff(self):
        list_game = self.board.moves[self.num_jugada].split("/")
        list_player = self.fen_notation[0:len(self.fen_notation)-1].split("/")
        error_list = []
        for i in range(8):
            error_list.append(self.get_diff_colum(list_game[i], list_player[i]))
        self.diagramador = Diagramador(self.ventana, True)
        self.diagramador.tablero.result_diff(error_list)
        self.fen_notation = ""

    def get_diff_colum(self, column1, column2):
        col = ''
        column1 = self.clen_format(column1)
        column2 = self.clen_format(column2)
        for i in range(8):
            if column1[i] != column2[i]:
                print(column1[i])
                col += 'f'
            else:
                col +=column1[i]
        return col
        
    def clen_format(self, column):
        cls_string = ''
        for c in column:
            if c.isnumeric():
                for i in range(int(c)):
                    cls_string += ','
            else:
                cls_string += c
        return cls_string

    def ListOnDoubleClick(self, event):
        item = self.position.curselection()
        self.num_jugada = int(item[0])
        self.board.move_pice(self.num_jugada)

    def OnDoubleClick(self, event):
        item = self._tree.identify('item',event.x,event.y)
        i = self._tree.item(self._tree.selection())['tags'][0]
        titulo = self._tree.item(self._tree.selection())['values'][4] + " vs " + self._tree.item(self._tree.selection())['values'][5]
        crea_tablero =  messagebox.askyesno(message="¿Desea visualizar la partida?", title="Crear tablero")
        if crea_tablero : 
            self.crea_tablero(i, titulo)

    def add_row(self, row):
        self._tree.insert('', 'end', values=row, tag=self.indice)
        self.indice += 1
        for i, item in enumerate(row):
            col_width = tkFont.Font().measure(item)
            if self._tree.column(self._headers[i], width=None) < col_width:
                    self._tree.column(self._headers[i], width=col_width + 20)

    def crea_tablero(self, i, titulo):
        self.board.fill_board()
        self.position.delete(0,tk.END)
        self.fen_notation = ''
        list = []
        aux = self.list_game[i].moves
        j=1
        for move in aux: 
            temp = str(j) + '.-' + str(move)
            self.position.insert(tk.END, temp)
            j+=1
        print(self.list_game[i].moves)
        self.fen_notation = self.FEN_parser.final_notation(aux)
        self.moves = self.fen_notation
        self.board.setMoves(self.fen_notation)
        self.num_jugada = 0

    def move(self, is_next):
        if (is_next):
            if self.num_jugada+1 < len(self.moves):
                self.num_jugada +=1
        else:
            if self.num_jugada-1 > 0:
                self.num_jugada -=1
        self.position.activate(self.num_jugada)
        self.board.move_pice(self.num_jugada)

    def last_move(self, is_end):
        if is_end:
            self.position.activate(len(self.moves)-1)
            self.board.move_pice(len(self.moves)-1)
        else:
            self.position.activate(0)
            self.board.move_pice(0)


if __name__ == "__main__":
    juego  = Principal()
    juego.ventana.mainloop() 