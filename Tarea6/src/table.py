import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
from tkinter import messagebox

class Table(tk.Frame):
    def __init__(self, parent=None, title="", headers=[], list_game=[], ventana=None,height=10, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self._title = tk.Label(self, text=title, background="#64d8cb", font=("Helvetica", 16), width=570, fg='black')
        self._headers = headers
        self.list_game = list_game
        self.ventana = ventana
        print(height-3)
        self._tree = ttk.Treeview(self,
                                  height=height-3,
                                  columns=self._headers, 
                                  show="headings")
        self._title.pack(side=tk.TOP, fill="x")
        self.id_card = -1

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
                              width=(tkFont.Font().measure(header.title()) * 3)+1)

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
        self.id_card = i