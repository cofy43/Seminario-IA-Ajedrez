class Fonst():
    def __init__(self):
        self.path = "partida_merida.txt"
        #self.font = font
        self.merida_pieces = {"Tbb.jpg" : "R", "Tbn.jpg" : "r", "Tnb.jpg" : "t", "Tnn.jpg" : "T",
                              "Cbb.jpg" : "N", "Cbn.jpg" : "n", "Cnb.jpg" : "M", "Cnn.jpg" : "m",
                              "Abb.jpg" : "B", "Abn.jpg" : "b", "Anb.jpg" : "V", "Ann.jpg" : "v",
                              "Dbb.jpg" : "Q", "Dbn.jpg" : "q", "Dnb.jpg" : "W", "Dnn.jpg" : "w",
                              "Rbb.jpg" : "k", "Rbn.jpg" : "K", "Rnb.jpg" : "L", "Rnn.jpg" : "l",
                              "Pbb.jpg" : "P", "Pbn.jpg" : "p", "Pnb.jpg" : "O", "Pnn.jpg" : "o",
                              "b.jpg" : " ", "n.jpg" : "+", "9" : "!\"\"\"\"\"\"\"\"#", 
                              "0" : "/(((((((()"}

        self.board_pieces = {"R" : "Tbb.jpg", "r" : "Tbn.jpg", "t" : "Tnb.jpg", "T" : "Tnn.jpg",
                             "N" : "Cbb.jpg", "n" : "Cbn.jpg", "M" : "Cnb.jpg", "m" : "Cnn.jpg",
                             "B" : "Abb.jpg", "b" : "Abn.jpg", "V" : "Anb.jpg", "v" : "Ann.jpg",
                             "Q" : "Dbb.jpg", "q" : "Dbn.jpg", "W" : "Dnb.jpg", "w" : "Dnn.jpg",
                             "k" : "Rbb.jpg", "K" : "Rbn.jpg", "L" : "Rnb.jpg", "l" : "Rnn.jpg",
                             "P" : "Pbb.jpg", "p" : "Pbn.jpg", "O" : "Pnb.jpg", "o" : "Pnn.jpg",
                             " " : "b.jpg", "+" : "n.jpg"}

        self.vertilcal_inicial = "$"
        self.vertilcal_final = "%"

    def guarda(self, board, path):
        file = open(path, "w")
        print(file)
        file.write("\n")
        file.write(self.merida_pieces["9"])
        file.write("\n")
        for r in range(8):
            row = self.vertilcal_inicial
            for c in range(8):
                piece = board[r][c]
                row = row + self.merida_pieces[piece]
            row = row + self.vertilcal_final
            file.write(row)
            file.write("\n")
        file.write(self.merida_pieces["0"])
        file.close()

    def lee(self, path):
        file = open(path, "r")
        i = -1
        j = 0
        board = {}
        for linea in file.readlines():
            print(i)
            print(linea)
            if (i > -1 and i < 8):
                for c in linea:
                    if (c == '$' or c == '%' or c == '\n' or c == '!' or c == '\"' or c == '#'):
                        print("no se lee")
                    else :
                        coordenada = "(" + str(i) + "," + str(j) + ")"
                        print(c)
                        piece = self.board_pieces[c]
                        board[coordenada] = piece
                        j = j + 1
            i = i +1
            j = 0
        print(board)
        file.close()
        return board

    #for name, age in mydict.items():
    #   if age == search_age:
    #       print name