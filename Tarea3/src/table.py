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
            newWindow = tk.Toplevel(self.ventana)
            newWindow.geometry("650x600")
            newWindow.title(titulo)
            self.tablero = Tablero(newWindow)
            self.tablero.pack()
            self.tablero.place(x=70, y = 70)
