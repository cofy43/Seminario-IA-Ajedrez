import parser as pgn
    
def lee():
    archivo = open('nuevo-london.pgn','r', encoding='utf-8', errors='ignore')
    lista = archivo.readlines()

    for linea in lista:
        # incrementa en 1 el contador  
        # muestra contador y elemento (línea)
        print(linea)
        print(type(linea))
    
    archivo.close()  # cierra archivo
lee()