import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
from tkinter import messagebox

from tablero import Tablero

class Table(tk.Frame):
    def __init__(self, parent=None, title="", headers=[], list_game=[], ventana=None,height=10, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self._title = tk.Label(self, text=title, background="#9086ba", font=("Helvetica", 16))
        self._headers = headers
        self.list_game = list_game
        self.ventana = ventana
        self._tree = ttk.Treeview(self,
                                  height=height,
                                  columns=self._headers, 
                                  show="headings")
        self._title.pack(side=tk.TOP, fill="x")
        self.num_jugada = -1

        # Agregamos dos scrollbars 
        vsb = ttk.Scrollbar(self, orient="vertical", command=self._tree.yview)
        vsb.pack(side='right', fill='y')
        hsb = ttk.Scrollbar(self, orient="horizontal", command=self._tree.xview)
        hsb.pack(side='bottom', fill='x')

        self._tree.configure(xscrollcommand=hsb.set, yscrollcommand=vsb.set)
        self._tree.pack(side="left")

        for header in self._headers:
            self._tree.heading(header, text=header.title())
            self._tree.column(header, stretch=True,
                              width=tkFont.Font().measure(header.title()))

        self._tree.bind("<Double-1>",self.OnDoubleClick)
        self.indice = 0

    def add_row(self, row):
        self._tree.insert('', 'end', values=row, tag=self.indice)
        self.indice += 1
        for i, item in enumerate(row):
            col_width = tkFont.Font().measure(item)
            if self._tree.column(self._headers[i], width=None) < col_width:
                    self._tree.column(self._headers[i], width=col_width + 20)

    def OnDoubleClick(self, event):
        item = self._tree.identify('item',event.x,event.y)
        print(self._tree.item(self._tree.selection()))
        i = self._tree.item(self._tree.selection())['tags'][0]
        titulo = self._tree.item(self._tree.selection())['values'][4] + " vs " + self._tree.item(self._tree.selection())['values'][5]
        crea_tablero =  messagebox.askyesno(message="¿Desea visualizar la partida?", title="Crear tablero")
        if crea_tablero : 
            self.crea_tablero(i, titulo)

    def move(self, is_next):
        print("move")
        if (is_next):
            if self.num_jugada+1 < len(self.tablero.moves):
                self.num_jugada +=1
            else:
                print("ocurrio un error al hacer la siguiente jugada")
        else:
            if self.num_jugada-1 >= 0:
                self.num_jugada -=1
            else:
                print("ocurrio un error al hacer la anterior jugada")

        self.tablero.move_pice(self.num_jugada)
    
    def crea_tablero(self, i, titulo):
        newWindow = tk.Toplevel(self.ventana)
        newWindow.geometry("650x420")
        newWindow.title(titulo)
        moves = self.list_game[i].moves

        next_move = tk.Button(newWindow, text="Adelante", command = lambda:self.move(True))
        next_move.pack()
        next_move.place(x=180, y=360)

        back_move = tk.Button(newWindow, text="Atras", command = lambda:self.move(False))
        back_move.pack()
        back_move.place(x=50, y=360)

        list = tk.Listbox(newWindow, width=18, height=20)
        jugada = ""
        j = 0
        result = self.list_game[i].header['result']
        i = 1
        leng = len(moves)

        for j in range(0, leng, 2):
            if (j <= leng):
                jugada += str(i) + ". " + moves[j]
            if (j+1 < leng):
                jugada += " " + moves[j+1]
        
            list.insert(tk.END, jugada)
            jugada = ""
            i += 1

        self.tablero = Tablero(newWindow, moves)
        self.tablero.pack()
        self.tablero.place(x=10, y=10)
            
        list.pack()
        list.place(x=460, y=10)