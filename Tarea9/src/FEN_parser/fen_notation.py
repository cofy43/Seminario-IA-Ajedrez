import chess

class Fen_notation():
    """
    Clase principal encargada de la ejecución del programa
    """
    def __init__(self) :
        self.game = None

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
        self.pgn = open(path)
        

    def final_notation(self, moves):
        """
        Funcion auxuliar encargada de mostrar 
        la conversion en formato FEN en el cuadro de
        texto despues de presionar el boton 
        correspondiente y tambien se encarga de activar
        el boton de copiar al porta papeles y de exportacion.
        """
        fen_string = []
        self.game = chess.Board()
        for move in moves:
            self.game.push_san(str(move))
            fen_string.append(self.clean_fen(self.game.fen()))

        return fen_string

    def clean_fen(self, fen_notation):
        i = fen_notation.index(' ')
        return fen_notation[0: i]