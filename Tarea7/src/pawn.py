import re

SPACE = " "
MAKE_EP_FROM = {"P": "5", "p": "4"}
MAKE_CAP_FROM = {"P": {"3": "2", "4":"3", "5": "4", "6": "5", "7": "6"},
                 "p": {"6": "7", "5": "6", "4": "5", "3": "4", "2": "3"}}
MAKE_PROM_FROM = {"P": "7", "p": "2"}
MAKE_REG_FROM = {"P": {"3": ["2"], "4": ["3", "2"],"5": ["4"],"6": ["5"],"7": ["6"]},
                 "p": {"6": ["7"], "5": ["6", "7"],"4": ["5"],"3": ["4"],"2": ["3"]}}

def make_pawn_move(move, board_view, piece_view):
    """
    Funcion principal encargada de la catalogacion
    y realizacion del movimineto del peon
    Parameters
    ----------
    move : string
        Incial del peon
    board_view : string
        Representacion en cadena del tablero
    piece_view : object
        Diccionario donde las llaves son las coordenadas del 
        tablero y los valores son las inciales de la pieza o
        un espacio vacio
    Returns
    -------
    string
        Representacion en cadena despues de efectuar el movimiento
    object 
        Diccionario donde las llaves son las coordenadas del 
        tablero y los valores son las inciales de la pieza o
        un espacio vacio posterior al movimineto del peon
    """
    if is_ep(move, board_view):
        print('is_ep')
        return make_ep(move, board_view, piece_view)
    elif is_capture(move):
        print('is_capture')
        return make_capture(move, board_view, piece_view)
    elif is_promotion(move):
        print('is_promotion')
        return make_promotion(move, board_view, piece_view)
    elif is_regular_move(move):
        print('is_regular_move')
        return make_regular_move(move, board_view, piece_view)

def is_ep(move, board_view):
    """
    FUncion auxiliar encargada de verificar si el movimiento 
    del peon es el primero para dicha pieza.
    Parameters
    ----------
    move : string
        inicial de la pieza peon
    board_view : string
        Representacion en cadena del tablero
    Returns
    -------
    boolean
        Verdadero o Falso segun sea el caso.
    """
    return re.fullmatch("[Pp][a-h]x[a-h][2-7]", move) is not None and board_view[move[-2:]] == SPACE

def is_capture(move):
    """
    Funcion auxiliar encargada de verificar si el
    movimiento del peon implica una captura.
    Parameters
    ----------
    move : string
        Incial del peon
    Returns
    -------
    boolean
        Verdadero o Falso segun sea el caso
    """
    return re.fullmatch("[Pp][a-h]x[a-h][2-7]", move) is not None

def is_promotion(move):
    """
    Funcion auxiliar encargada de verificar 
    si el peon ha llegado a la octava fila en caso de
    las blancas o a la primera en caso de las negras.
    Parameters
    ----------
    move : string
        Incial del peon
    Returns
    -------
    boolean
        Verdadero o Falso segun sea el caso.
    """
    return re.fullmatch("[Pp][a-h](x[a-h])?[18][RNBQrnbq]", move) is not None

def is_regular_move(move):
    """
    Funcion auxiliar encargada de verificar si el 
    movimiennto del peon es un movimineto simple.
    Parameters
    ----------
    move : string
        Incial del peon
    Returns
    -------
    boolean
        Verdadero o false segun sea el caso.
    """
    return re.fullmatch("[Pp][a-h][2-7]", move) is not None

def make_ep(move, board_view, piece_view):
    """
    Funcion auxiliar encargada de realizar el
    movimiento de dos casillas para el peon
    Parameters
    ----------
    move : string
        Incial del peon
    board_view : string
        Representacion en cadena del tablero
    piece_view : object
        Diccionario donde las llaves son las coordenadas del 
        tablero y los valores son las inciales de la pieza o
        un espacio vacio
    Returns
    -------
    string
        Representacion en cadena despues de efectuar el movimiento
    object 
        Diccionario donde las llaves son las coordenadas del 
        tablero y los valores son las inciales de la pieza o
        un espacio vacio posterior al movimineto del peon
    """
    pawn, to_sq, from_file = move[0], move[-2:], move[1]
    from_sq = from_file + MAKE_EP_FROM[pawn]
    if pawn == "P":
        cap_at_sq = to_sq[0] + str(int(to_sq[1]) - 1)
    else:
        cap_at_sq = to_sq[0] + str(int(to_sq[1]) + 1)
    
    board_view[from_sq] = SPACE
    board_view[to_sq] = pawn
    board_view[cap_at_sq] = SPACE
    piece_view[pawn].append(to_sq)
    piece_view[pawn].remove(from_sq)
    piece_view[pawn.swapcase()].remove(cap_at_sq)

    return board_view, piece_view

def make_capture(move, board_view, piece_view):
    """
    Funcion auxiliar encargada de realizar la captura de 
    la pieza en cuestion.
    Parameters
    ----------
    move : string
        Incial del peon
    board_view : string
        Representacion en cadena del tablero
    piece_view : object
        Diccionario donde las llaves son las coordenadas del 
        tablero y los valores son las inciales de la pieza o
        un espacio vacio
    Returns
    -------
    string
        Representacion en cadena despues de efectuar el movimiento
    object 
        Diccionario donde las llaves son las coordenadas del 
        tablero y los valores son las inciales de la pieza o
        un espacio vacio posterior al movimineto del peon
    """
    pawn, to_sq, from_file = move[0], move[-2:], move[1]
    from_sq = from_file + MAKE_CAP_FROM[pawn][to_sq[1]]
    captured_piece = board_view[to_sq]

    board_view[from_sq] = SPACE
    board_view[to_sq] = pawn
    piece_view[pawn].append(to_sq)
    piece_view[pawn].remove(from_sq)
    piece_view[captured_piece].remove(to_sq)

    return board_view, piece_view

def make_promotion(move, board_view, piece_view):
    """
    Funcion auxiliar encargada de realizar el cambio
    del peon por la pieza seleccionado por el jugador
    tras haber llegado a la ultima fila en caso de las 
    blancas o a la primera en caso de las negras.
    Parameters
    ----------
    move : string
        Incial del peon
    board_view : string
        Representacion en cadena del tablero
    piece_view : object
        Diccionario donde las llaves son las coordenadas del 
        tablero y los valores son las inciales de la pieza o
        un espacio vacio
    Returns
    -------
    string
        Representacion en cadena despues de efectuar el movimiento
    object 
        Diccionario donde las llaves son las coordenadas del 
        tablero y los valores son las inciales de la pieza o
        un espacio vacio posterior al movimineto del peon
    """
    pawn, to_sq, promoted_to = move[0], move[-3:-1], move[-1]
    if "x" in move:
        from_file = move[1]
        captured_piece = board_view[to_sq]
    else:
        from_file = to_sq[0]
        captured_piece = SPACE
    from_sq = from_file + MAKE_PROM_FROM[pawn]

    board_view[to_sq] = promoted_to
    board_view[from_sq] = SPACE
    piece_view[pawn].remove(from_sq)
    piece_view[promoted_to].append(to_sq)
    if captured_piece != SPACE:
        piece_view[captured_piece].remove(to_sq)

    return board_view, piece_view

def make_regular_move(move, board_view, piece_view):
    """
    Funcion auxiliar encargada de realizar el movimiento
    traducional de una casilla del peon.
    Parameters
    ----------
    move : string
        Incial del peon
    board_view : string
        Representacion en cadena del tablero
    piece_view : object
        Diccionario donde las llaves son las coordenadas del 
        tablero y los valores son las inciales de la pieza o
        un espacio vacio
    Returns
    -------
    string
        Representacion en cadena despues de efectuar el movimiento
    object 
        Diccionario donde las llaves son las coordenadas del 
        tablero y los valores son las inciales de la pieza o
        un espacio vacio posterior al movimineto del peon
    """
    pawn, to_sq, from_file = move[0], move[-2:], move[-2]
    if len(MAKE_REG_FROM[pawn][to_sq[1]]) == 1:
        from_rank = MAKE_REG_FROM[pawn][to_sq[1]][0]
    else:
        for rank in MAKE_REG_FROM[pawn][to_sq[1]]:
            if board_view[from_file + rank] == pawn:
                from_rank = rank
                break
    from_sq = from_file + from_rank

    board_view[from_sq] = SPACE
    board_view[to_sq] = pawn
    piece_view[pawn].append(to_sq)
    piece_view[pawn].remove(from_sq)

    return board_view, piece_view
