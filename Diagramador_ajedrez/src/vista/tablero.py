import tkinter as tk

class Tablero(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.filas = 8
        self.columnas = 8
        self.dim_casilla = 40
        self.color_casillas = "white"
        self.dim_borde=0
        self.el_tablero = tk.Canvas(
            width=(350),
            height=(350)
            )
    
        self.el_tablero.pack()
        self.el_tablero.place(x=189, y = 155)
        self.fill_board()
        self.el_tablero.bind("<Button-1>", self.on_board_click, self.resize)

    def fill_board(self):
        # vamos a pintar un tablero de 8x8
        for r in range(self.filas):
            for c in range(self.columnas):
                id_casilla = (
                    f"{r + 1:0{len(str(self.filas))}d}|"
                    f"{c + 1:0{len(str(self.columnas))}d}")
                x1, y1 = c * self.dim_casilla, r * self.dim_casilla
                x2, y2 = x1 + self.dim_casilla, y1 + self.dim_casilla 
                self.el_tablero.create_rectangle(
                    x1, y1, x2, y2,
                    fill=self.color_casillas,
                    tags=id_casilla
                    )

    def on_board_click(self, event):
        columna = (event.x - self.dim_borde) // self.dim_casilla
        fila = (event.y - self.dim_borde) // self.dim_casilla
        id_casilla = (
            f"{fila + 1:0{len(str(self.filas))}d}|"
            f"{columna + 1:0{len(str(self.columnas))}d}")
        self.el_tablero.itemconfig(id_casilla, fill='blue')
        print("columa: " + str(columna) + " fila: " + str(fila))

    def resize(self, event):
        w,h = event.width-100, event.height-100
        self.c.config(width=w, height=h)