import tkinter as tk
from PIL import ImageTk, Image
import os

class Tablero(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.filas = 8
        self.path = "piezas-ajedrez/"
        self.columnas = 8
        self.piece = ""
        self.dim_casilla = 40
        self.color_casillas = "white"
        self.dim_borde=0
        self.el_tablero = tk.Canvas(
            width=(350),
            height=(350)
            )
        self.esBlanco = True
        self.pieces = {}
        self.board = [[0]*8 for i in range(8)]
        self.el_tablero.pack()
        self.el_tablero.place(x=189, y = 155)
        self.fill_board()
        self.el_tablero.bind("<Button-1>", self.on_board_click, self.resize)


    def fill_board(self):
        # vamos a pintar un tablero de 8x8
        for r in range(self.filas):
            for c in range(self.columnas):
                temp = ""

                if ((r+(c+1)) % 2 != 0) :
                    coordenada = "(" + str(c) + "," + str(r) + ")"
                    temp = "b.jpg"
                else :
                    coordenada = "(" + str(c) + "," + str(r) + ")"
                    temp = "n.jpg"

                photo = ImageTk.PhotoImage(Image.open(os.path.join(self.path,temp)))
                self.pieces[coordenada] = photo
                self.board[r][c] = temp
                image_id = self.el_tablero.create_image(((c*40), (r*40)+41), image = photo, anchor='sw')
                self.el_tablero.itemconfigure(image_id, image=self.pieces[coordenada])

    def setPiece(self, piece):
        self.piece = piece

    def on_board_click(self, event):
            if len(self.piece) > 0 :
                columna = ((event.x - self.dim_borde) // self.dim_casilla)
                fila = ((event.y - self.dim_borde) // self.dim_casilla)
                coodenada = "(" + str(columna) + "," + str(fila) + ")"

                if ((fila+(columna+1)) % 2 != 0) :
                    self.piece = self.piece + "b.jpg"
                else :
                    self.piece = self.piece + "n.jpg"

                try:
                    photo = ImageTk.PhotoImage(Image.open(self.path + self.piece))
                    self.pieces[coodenada] = photo
                    self.board[fila][columna] = self.piece
                    image_id = self.el_tablero.create_image(((columna*40), (fila*40)+41), image = photo, anchor='sw')
                except FileNotFoundError as e:
                    return
                except:
                    return
                
                try:
                    self.el_tablero.itemconfigure(image_id, image=self.pieces[coordenada])
                    self.el_tablero.photo = photo
                    self.piece = ""
                except NameError as e:
                    return
                except:
                    return
                    raise

    def getTablero(self):
        return self.board

    def getCoordenadaX(self, coordenada):
        return int(coordenada[1])

    def getCoordenadaY(self, coordenada):
        return int(coordenada[3])

    def setTablero(self, board):
        for coordenada, piece in board.items():
            x = self.getCoordenadaX(coordenada)
            y = self.getCoordenadaY(coordenada)
            photo = ImageTk.PhotoImage(Image.open(self.path + piece))
            self.pieces[coordenada] = photo
            self.board[x][y] = piece
            image_id = self.el_tablero.create_image(((y*40), (x*40)+41), image = photo, anchor='sw')
            self.el_tablero.itemconfigure(image_id, image=self.pieces[coordenada])

    def resize(self, event):
        w,h = event.width-100, event.height-100
        self.c.config(width=w, height=h)