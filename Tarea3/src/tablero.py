import tkinter as tk
from PIL import ImageTk, Image
import os

class Tablero(tk.Frame):
    def __init__(self, parent, moves=[], *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.filas = 8
        self.path = "piezas-ajedrez/"
        self.parent = parent
        self.columnas = 8
        self.images = []
        self.moves = moves
        self.arrows = {}
        self.num_arrows = 0
        self.rectangles = []
        self.tempx, self.tempy = 0, 0
        self.piece = ""
        self.color = "none"
        self.dim_casilla = 40
        self.color_casillas = "white"
        self.dim_borde=0
        self.el_tablero = tk.Canvas(
            self.parent,
            width=(320),
            height=(320)
            )
        self.pieces = {}
        self.piezas = {}
        self.id_pieces = []
        self.board = [[0]*8 for i in range(8)]
        self.el_tablero.pack()
        self.el_tablero.place(x=20, y = 20)
        self.fill_board()
        self.el_tablero.bind("<Button-1>", self.on_board_click, self.resize)
        self.el_tablero.bind("<ButtonPress-3>",self.boton_presion)
        self.el_tablero.bind("<ButtonRelease-3>",self.boton_soltar)
        self.el_tablero.bind('<Shift-Button-1>', self.key)
        print(self.piezas)

        self.presionado=False
        self.pieza = {"K":"R", "Q":"D", "R":"T", "B":"A", "N":"C", "P":"P"}
        self.columna = { "a":"0", "b":"1", "c":"2", "d":"3", "e":"4", "f":"5", "g":"6", "h":"7"} 

    def key(self,event):
        if self.color != 'none':
            tuple_objects = self.el_tablero.find_closest(event.x, event.y, halo = 5)
            if len(tuple_objects) > 0:
                objectToBeDeleted = tuple_objects[0]
                if not(objectToBeDeleted in self.id_pieces):
                    self.el_tablero.delete(objectToBeDeleted)


    def fill_board(self):
        temp = ""
        is_piece = False
        is_peon = False
        piece = ""
        for r in range(self.filas):
            for c in range(self.columnas):

                if (r == 0 or r == 1) :
                    temp += "n"
                    if (r == 0):
                        is_piece = True
                        is_peon = False 
                    else:
                        is_peon = True
                        is_piece = False

                elif r == 7 or r == 6:
                    temp += "b"
                    if (r == 7):
                        is_piece = True
                        is_peon = False
                    else :
                        is_peon = True 
                        is_piece = False

                elif r > 1 and r < 6:
                    is_piece = False
                    is_peon = False


                #Se crean los peones
                if (is_peon) :
                    temp = "P" + temp
                    piece = "P"

                elif (is_piece):
                    #Se crean las piezas de acuerdo a la columna
                    if (c == 0 or c == 7) and is_piece:
                        temp = "T" + temp
                        piece = "T"
                    if (c == 1 or c == 6) and is_piece:
                        temp = "C" + temp
                        piece = "C"
                    if (c == 2 or c == 5) and is_piece:
                        temp = "A" + temp
                        piece = "A"
                    if (c == 3) and is_piece:
                        temp = "D" + temp
                        piece = "D"
                    if (c == 4) and is_piece:
                        temp = "R" + temp
                        piece = "R"

                if ((r+(c+1)) % 2 != 0) :
                    temp = temp + "b.jpg"
                else :
                    temp = temp + "n.jpg"

                coordenada = "(" + str(c) + "," + str(r) + ")"

                photo = ImageTk.PhotoImage(Image.open(os.path.join(self.path,temp)))
                self.pieces[coordenada] = photo
                self.piezas[coordenada] = piece
                self.board[r][c] = temp
                image_id = self.el_tablero.create_image(((c*40), (r*40)+41), image = photo, anchor='sw')
                self.id_pieces.append(image_id)
                self.el_tablero.itemconfigure(image_id, image=self.pieces[coordenada])
                temp = ""
                piece = ""

    def setPiece(self, piece):
        self.piece = piece

    def set_color(self, color):
        self.color = color

    def create_rectangle(self,columna, fila, **kwargs):
        id_casilla = str(fila + 1).zfill(2) +  str(columna + 1).zfill(2)
        x1, y1 = columna * self.dim_casilla, fila * self.dim_casilla
        x2, y2 = x1 + self.dim_casilla, y1 + self.dim_casilla 

        if 'alpha' in kwargs:
            alpha = int(kwargs.pop('alpha') * 255)
            fill = kwargs.pop('fill')
            fill = self.el_tablero.winfo_rgb(fill) + (alpha,)
            image = Image.new('RGBA', (x2-x1, y2-y1), fill)
            self.images.append(ImageTk.PhotoImage(image))
            self.el_tablero.create_image(x1, y1, image=self.images[-1], anchor='nw')
            try:
                print(temp)
            except NameError as e:
                return
        
        self.el_tablero.create_rectangle(x1, y1, x2, y2 , **kwargs)

    def crea_pieza(self,columna,fila):
        coodenada = "(" + str(columna) + "," + str(fila) + ")"   
        if ((fila+(columna+1)) % 2 != 0) :
            if (self.piece == "trash") :
                self.piece = "b.jpg"
            else:
                self.piece = self.piece + "b.jpg"
        else :
            if (self.piece == "trash") :
                self.piece = "n.jpg"
            else: 
                self.piece = self.piece + "n.jpg"

        try:
            photo = ImageTk.PhotoImage(Image.open(self.path + self.piece))
            self.pieces[coodenada] = photo
            self.piezas[coodenada] = piece
            self.board[fila][columna] = self.piece
            self.id_pieces.append(photo)
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

    def on_board_click(self, event):
        columna = ((event.x - self.dim_borde) // self.dim_casilla)
        fila = ((event.y - self.dim_borde) // self.dim_casilla)
        if len(self.piece) > 0 :
            self.crea_pieza(columna, fila)
            self.piece = ""
        else :
            if self.color != "none":
                self.create_rectangle(columna, fila, fill=self.color, alpha=0.5)

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

    def boton_soltar(self,event):
        self.presionado=False
        if self.color != 'none':
            columna = ((event.x - self.dim_borde) // self.dim_casilla)
            fila = ((event.y - self.dim_borde) // self.dim_casilla)
            columna0 = ((self.origenx - self.dim_borde) // self.dim_casilla)
            fila0 = ((self.origeny - self.dim_borde) // self.dim_casilla)
            coodenada = "(" + str(columna0) + "," + str(fila0) + ")"
            temp = self.el_tablero.create_line((columna0*40)+20, (fila0*40)+20, (columna*40)+20, (fila*40)+20, width =10, fill=self.color, arrow=tk.LAST)
            self.el_tablero.create_line((columna0*40)+20, (fila0*40)+20, (columna*40)+20, (fila*40)+20, width =10, fill=self.color, arrow=tk.LAST)
            self.arrows[coodenada] = temp

    def boton_presion(self, evento):
        self.presionado=True
        self.origenx=evento.x
        self.origeny=evento.y

    def move_pice(self, i):
        print(self.moves[i])
        move = self.moves[i]
        coordenada = ""
        is_peon = False

        if move.find("O") > 0:
            print("falta enrroque")
        else:

            if len(move) >= 3:
                print(move[1], move[2])
                coordenada = self.construye_coordenada(move[1], move[2])
                
            else:
                is_peon = True
                print(move[0], move[1])
                coordenada = self.construye_coordenada(move[0], move[1])

            print(coordenada)
            if (self.piezas[coordenada] != ""):
                if is_peon:
                    self.piece = "P"
                else: 
                    self.piece = self.pieza[move[0]] 
                self.crea_pieza(coordenada[1],coordenada[3])


    def construye_coordenada(self, c, f):
        return "(" + self.columna[c] + "," + str(f) + ")"        
