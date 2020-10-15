import parser as pgn
    
def lee():
    archivo = open('nuevo-london.pgn','r', encoding='utf-8', errors='ignore')
    lista = archivo.readlines()
    numlin=0

    for linea in lista:
        # incrementa en 1 el contador  
        numlin += 1
        # muestra contador y elemento (línea)
        print(numlin, linea)
    
    archivo.close()  # cierra archivo
lee()