import tkinter as tk
from PIL import ImageTk, Image
import os

class Tablero(tk.Frame):
    def __init__(self, parent, is_diagram,*args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.filas = 8
        self.path = "piezas-ajedrez/"
        self.parent = parent
        self.columnas = 8
        self.is_diagram =is_diagram
        self.images = []
        self.moves = []
        self.arrows = {}
        self.num_arrows = 0
        self.rectangles = []
        self.tempx, self.tempy = 0, 0
        self.piece = ""
        self.color = "none"
        self.dim_casilla = 40
        self.create = True
        self.color_casillas = "white"
        self.dim_borde=0
        self.el_tablero = tk.Canvas(
            self.parent,
            width=320,
            height=320,
            bd=0
            )
        self.pieces = {}
        self.piezas = {}
        self.id_pieces = []
        self.board = [[0]*8 for i in range(8)]
        self.el_tablero.pack()
        self.el_tablero.place(x=0, y = 0)
        self.fill_board()

        self.presionado=False
        self.pieza = {"K":"R", "Q":"D", "R":"T", "B":"A", "N":"C", "P":"P"}
        self.pieza_traduccion = {"R":"K", "D":"Q", "T":"R", "A":"B", "C":"N", "P":"P"}
        self.columna = { "a":"0", "b":"1", "c":"2", "d":"3", "e":"4", "f":"5", "g":"6", "h":"7"} 
        self.el_tablero.bind("<Button-1>", self.on_board_click, self.resize)

    def key(self,event):
        if self.color != 'none':
            tuple_objects = self.el_tablero.find_closest(event.x, event.y, halo = 5)
            if len(tuple_objects) > 0:
                objectToBeDeleted = tuple_objects[0]
                if not(objectToBeDeleted in self.id_pieces):
                    self.el_tablero.delete(objectToBeDeleted)

    def setPiece(self, piece):
        if self.is_diagram:
            self.piece = piece

    def on_board_click(self, event):
        if self.is_diagram:
            if len(self.piece) > 0 :
                columna = ((event.x - self.dim_borde) // self.dim_casilla)
                fila = ((event.y - self.dim_borde) // self.dim_casilla)
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
                    self.board[fila][columna] = self.piece
                    image_id = self.el_tablero.create_image(((columna*40), (fila*40)+41), image = photo, anchor='sw')
                except FileNotFoundError as e:
                    return
                except:
                    return
                
                try:
                    self.el_tablero.itemconfigure(image_id, image=self.pieces[coordenada])
                    self.el_tablero.photo = photo
                    #self.piece = ""
                except NameError as e:
                    return
                except:
                    return
                    raise
        
    def fill_board(self):
        temp = ""
        is_piece = False
        is_peon = False
        piece = ""
        for r in range(self.filas):
            for c in range(self.columnas):

                if not self.create:
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
            self.board[columna][fila] = self.piece
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


    def move_pice(self, i):        
        self.fill_board()
        move = self.moves[i].split('/')        
        i, j = 0, 0
        for line in move:            
            for c in line:
                if c.isnumeric():
                    self.piece = 'trash'
                    self.crea_pieza(j, i)
                    for k in range(-1,int(c)-1, 1):
                        j+=1
                        self.crea_pieza(j, i)
                        self.piece = ""
                    j-=1
                else:
                    self.piece = self.pieza[c.capitalize()]
                    if c.islower():
                        self.piece += 'n'
                    else:
                        self.piece += 'b'
                    self.crea_pieza(j, i)
                j+=1
                self.piece = ""
                
            i+=1
            j=0

    def result_diff(self, move):        
        self.fill_board()
        i, j = 0, 0
        for line in move:            
            for c in line:
                if c == ',':
                    self.piece = 'trash'
                    self.crea_pieza(j, i)
                elif c == 'f':
                    self.piece = 'error'
                    self.crea_pieza(j, i)
                    self.piece = ""
                else:
                    self.piece = self.pieza[c.capitalize()]
                    if c.islower():
                        self.piece += 'n'
                    else:
                        self.piece += 'b'
                    self.crea_pieza(j, i)
                j+=1
                self.piece = ""
                
            i+=1
            j=0

    def setMoves(self, moves):
        self.create = False
        self.fill_board()
        self.moves = []
        self.moves = moves

    def get_fen(self):
        fen = ''
        count = 0
        for r in range(self.filas):
            for c in range(self.columnas):
                temp = self.board[r][c]
                if len(temp) == 5:
                    count += 1
                else:
                    if count != 0:
                        fen += str(count) + self.get_piece(temp) 
                        count = 0
                    else:
                        fen += self.get_piece(temp) 
                    
            if count != 0:
                fen += str(count)
                count = 0
            fen += '/'
        return fen

    def get_piece(self, image):
        i = image.index('.')
        aux = image[0:i]
        if aux[1] == 'n':
            return self.pieza_traduccion[aux[0]].lower()
        return self.pieza_traduccion[aux[0]]