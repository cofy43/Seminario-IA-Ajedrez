import re

def pgn_to_moves(moves):
    """
    Funcion principal encargada de obtener
    las jugadas de la partida en formato png.
    Parameters
    ----------
    raw_pgn : string
        Lectura de la partida en formato png en una
        sola linea.
    Returns
    -------
    object 
        Lista de tuplas donde cada tupla incluye el movimineto
        del jugador de las piezas blancas y el segundo el
        movimineto de las piezas negras.
    
    comments_marked = raw_pgn.replace("{","<").replace("}",">")
    STRC = re.compile("<[^>]*>")
    comments_removed = STRC.sub(" ", comments_marked)

    STR_marked = comments_removed.replace("[","<").replace("]",">")
    str_removed = STRC.sub(" ", STR_marked)

    MOVE_NUM = re.compile("[1-9][0-9]* *\.")
    just_moves = [_.strip() for _ in MOVE_NUM.split(str_removed)]

    last_move = just_moves[-1]
    RESULT = re.compile("( *1 *- *0 *| *0 *- *1 *| *1/2 *- *1/2 *)")
    last_move = RESULT.sub("", last_move)
    moves = just_moves[:-1] + [last_move]
    moves = clean(moves)
    """
    return pre_process_moves(moves)

def clean(moves):
    """
    Funcion auxiliar de normalizar el texto para
    la creacion de la lista de tuplas con los movimientos
    de la partida.
    Parameters
    ----------
    moves : object
        Lista de tuplas sin normalizar.
    Returns
    -------
    object 
        Lista de tuplas normalizada.
    """
    cleaned_moves = []
    for move in moves:
        if "e.p." in move:
            cleaned_move = move.replace("e.p.", "")
        SPECIAL_CHARS = re.compile("[^a-zA-Z0-9 ]")
        cleaned_move = SPECIAL_CHARS.sub("", move)
        cleaned_moves.append(cleaned_move)
    
    return cleaned_moves

def pre_process_a_move(move):
    """
    Funcion auxiliar encargada de dar estructura
    a la lista de tuplas con las jugadas de la partida.
    Parameters
    ----------
    moves : object
        Lista de tuplas con las jugadas
    Returns
    -------
    moves : object
        Lista de tuplas con las jugadas con la coordenada
        a donde debe de ir la pieza.
    """
    if len(move.split()) == 1:
        wmove = move
        if wmove[0] in "abcdefgh":
            wmove = "P" + wmove
        return (wmove, )
    wmove, bmove = move.split()
    if wmove[0] in "abcdefgh":
        wmove = "P" + wmove
    if bmove[0] in "abcdefgh":
        bmove = "p" + bmove
    bmove = bmove.lower()
    
    return wmove, bmove

def pre_process_moves(moves):
    """
    Funcion auxiliar encargada de eliminar las jugadas
    nulas.
    Parameters
    ----------
    moves : string
        Lista de tuplas con posibles jugadas nulas (vacias).
    Returns
    -------
    moves : string
        Lista de tuplas sin posibles jugadas nulas (vacias).
    """
    return [pre_process_a_move(move) for move in moves if len(move) > 0]
