import tkinter as tk
import tkinter.font as tkFont
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image

import pgn_parser
import piece
import pawn

class Main():
    """
    Clase principal encargada de la ejecución del programa
    """
    def __init__(self) :
        self.path = ''
        self.pgn = None
        self.fen = None
        self.fen_notation = None
        self.raw_pgn = None
        self.ventana = tk.Tk()
        self.ventana.geometry("742x550")
        self.ventana.title("Convertidor PGN a FEN")
        self.ventana['bg'] = '#4db6ac'
        self.png_label = tk.Label(self.ventana, text='Formato PNG:', bg='#4db6ac')
        self.png_label.place(x=30, y=130)
        self.png = tk.Text(self.ventana, width=40, height=18)
        self.png.place(x=30, y=150)
        self.fen_label = tk.Label(self.ventana, text='Formato FEN:', bg='#4db6ac')
        self.fen_label.place(x=380, y=130)
        self.fen = tk.Text(self.ventana, width=40, height=18)
        self.fen.place(x=380, y=150)
        self.moves = ''
        self.read_file = tk.Button(self.ventana, text="Leer partida", command = self.read_file, bg='#82e9de')
        self.read_file.place(x=40, y=40)
        self.to_fen = tk.Button(self.ventana, text="Convertir a FEN", command = self.final_notation, state=tk.DISABLED, bg='#82e9de')
        self.to_fen.place(x=180, y=40)
        self.copy = tk.Button(self.ventana, text="Copiar", command = self.copy_to_clipboard, state=tk.DISABLED, bg='#82e9de')
        self.copy.place(x=340, y=40)
        self.export = tk.Button(self.ventana, text="Guardar formato FEN", command = self.salvar_partida, state=tk.DISABLED, bg='#82e9de')
        self.export.place(x=450, y=40)

        self.ventana.mainloop()

    def read_file(self):
        """
        Función encargada de la lectura de la partida en formato
        pgn y que se encarga de mostrarla en el cuadro de texto
        para su visualización.
        """
        try:
            path = filedialog.askopenfilename(title="Abrir partida", initialdir="./", filetypes=[("Text files","*.pgn")])
            self.set_game(path)
            self.moves = pgn_parser.pgn_to_moves(self.raw_pgn)
            self.to_fen['state'] = tk.NORMAL
        except FileNotFoundError as e:
            messagebox.showerror(title="ERROR", message="No se encontro el archivo indicado")
    
    def set_game(self, path):
        """
        Función encargada de escribir la partida previamente
        leida en el cuadro de texto correspondiente.
        Parameters
        ----------
        path : string
            Ruta relativa de la ubicación del archivo pgn con la o
            las partidas que el usuario ha seleccionado
        """
        self.raw_pgn = " ".join([line.strip() for line in open(path)])
        self.png.delete('1.0', tk.END)
        self.png.insert(tk.END, self.raw_pgn)

    def setup(self):
        """
        Función auxiliar encargada de crear la representación 
        del tablero con una cadena y la creación del un 
        diccionario donde se encuentran las coordenadas de las
        del tablero para mantener registro de la partida
        Returns
        -------
        board_view: string
            Representación en cadena del tablero.
        piece_view: object
            Diccionario con las coordenadas como llave y como valor 
            la representacion de la pieza (mayusculas blancas, minusculas
            negras en idioma ingles) o espacios vacios.
        """
        squares = [y+x for x in "12345678" for y in "abcdefgh"]
        start = "RNBQKBNR" + "P" * 8 + " " * 32 + "p" * 8 + "rnbqkbnr"
        
        board_view = {square: piece for square, piece in zip(squares, start)}
        piece_view = {_: [] for _ in "BKNPQRbknpqr"}
        for sq in board_view:
            piece = board_view[sq]
            if piece != " ":
                piece_view[piece].append(sq)
        
        return board_view, piece_view

    def convert_to_fen(self, board_view):
        """
        Funcion auxiliar encargada de converir una partida 
        en formato FEN dada una representacion en cadena
        del tablero.
        Parameters
        ----------
        board_view : string
            Representación del tablero en una cadena
        Returns
        -------
        string
            Cadena en formato FEN.
        """
        pieces = list(board_view.values())
        fen = ""
        for i in range(8):
            row = pieces[(i * 8): (i + 1) * 8]
            fen += "".join(row) + "/"
        print(fen)
        return self.replace_spaces(fen)

    def replace_spaces(self, fen):
        """
        Funcion auxiliar que elimina los espacios y los 
        convierte en numeros para tener una completa y 
        correcta cadena en formato FEN
        Parameters
        ----------
        fen : string
            Cadena en formato FEN con espacios
        Returns
        -------
        string
            Cadena en formato FEN con numeros
            en lugar de espacios
        """
        for i in range(8, 0, -1):
            if " " * i in fen:
                fen = fen.replace(" " * i, str(i))
        return fen[:-1]

    def make_one_move(self, move, board_view, piece_view):
        """
        Funcion auxuliar encargada de hacer la distincion 
        de los movimientos entre las piezas, el enroque
        y los peones para relevar la accion del movimiento
        a sus respectivas clases. Finalmente devuelve la 
        representación en cadena del tablero y el diccionario
        con las coordenadas, ambos resultantes despues de 
        realizar los movimientos de dicha pieza.
        Parameters
        ----------
        move : string
            Cadena encargada de representar que pieza 
            se movera, tomando como un caso especial el enroque.
        board_view : string
            Representacion en cadena del tablero.
        piece_view : object
            Diccionario de las coordenadas donde el valor
            es la inicial de la pieza o un espacio vacio
        Returns
        -------
        string
            Representacion en cadena del tablero
        object
            Diccionario donde las llaves son las 
            coordenadas del tablero y el valor es
            la inicial de la pieza o un espacio en 
            blanco
        """
        if move in "OOOooo":
            return piece.castle(move, board_view, piece_view)
        elif move[0] in "Pp":
            return pawn.make_pawn_move(move, board_view, piece_view)
        else:
            return piece.move_piece(move, board_view, piece_view)

    def make_moves(self):
        """
        Funcion principal encargada de realizar cada uno
        de los movimiento de la partida en png previamente
        leida y por medio de una cadena realizar su conversion 
        de la misma en formato FEN.
        Returns
        -------
        string
            Representacion en cadena de la partida en formato FEN.
        """
        board_view, piece_view = self.setup()
        fen = ''
        for move in self.moves[:-1]:
            wmove, bmove = move
            board_view, piece_view = self.make_one_move(wmove, board_view, piece_view)
            fen += self.convert_to_fen(board_view) + '\n'
            board_view, piece_view = self.make_one_move(bmove, board_view, piece_view)
            fen += self.convert_to_fen(board_view) + '\n'

        if len(self.moves[-1]) == 1:
            wmove = self.moves[-1][0]
            board_view, piece_view = self.make_one_move(wmove, board_view, piece_view)
            fen += self.convert_to_fen(board_view) + '\n'
        else:
            wmove, bmove = self.moves[-1]
            board_view, piece_view = self.make_one_move(wmove, board_view, piece_view)
            fen += self.convert_to_fen(board_view) + '\n'
            board_view, piece_view = self.make_one_move(bmove, board_view, piece_view)
            fen += self.convert_to_fen(board_view) + '\n'

        return fen

    def final_notation(self):
        """
        Funcion auxuliar encargada de mostrar 
        la conversion en formato FEN en el cuadro de
        texto despues de presionar el boton 
        correspondiente y tambien se encarga de activar
        el boton de copiar al porta papeles y de exportacion.
        """
        self.fen_notation = self.make_moves()
        self.fen.delete('1.0', tk.END)
        self.fen.insert(tk.END, self.fen_notation)
        self.copy['state'] = tk.NORMAL
        self.export['state'] = tk.NORMAL

    def copy_to_clipboard(self):
        """
        Funcion auxiliar encargada de copiar la partida 
        en formato FEN al portapapeles del usuario.
        """
        self.ventana.clipboard_clear()
        self.ventana.clipboard_append(self.fen_notation)

    def salvar_partida(self):
        """
        Funcion auxiliar encargada de abrir un explorador
        de archivos y almacenar la partida en formato FEN.
        """
        path = filedialog.asksaveasfilename(title = "Guardar partida", defaultextension=".fen", filetypes=[("Text files","*.fen")])
        file = open(path, "w")
        file.write(self.fen_notation)
        file.close()

if __name__ == "__main__":
    exe = Main()
    pass