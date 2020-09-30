class Fonst():
    def __init__(self):
        self.path = "partida_merida.txt"
        #self.font = font
        self.merida_pieces = {"Tbb.jpg" : "r", "Tbn.jpg" : "R", "Tnb.jpg" : "t", "Tnn.jpg" : "T",
                              "Cbb.jpg" : "n", "Cbn.jpg" : "N", "Cnb.jpg" : "m", "Cnn.jpg" : "M",
                              "Abb.jpg" : "b", "Abn.jpg" : "B", "Anb.jpg" : "v", "Ann.jpg" : "V",
                              "Dbb.jpg" : "q", "Dbn.jpg" : "Q", "Dnb.jpg" : "w", "Dnn.jpg" : "W",
                              "Rbb.jpg" : "k", "Rbn.jpg" : "K", "Rnb.jpg" : "l", "Rnn.jpg" : "L",
                              "Pbb.jpg" : "p", "Pbn.jpg" : "P", "Pnb.jpg" : "o", "Pnn.jpg" : "O",
                              "b.jpg" : " ", "n.jpg" : "+", "9" : "!\"\"\"\"\"\"\"\"#", 
                              "0" : "/(((((((()"}

        self.board_pieces = {"r" : "Tbb.jpg", "R" : "Tbn.jpg", "t" : "Tnb.jpg", "T" : "Tnn.jpg",
                             "n" : "Cbb.jpg", "N" : "Cbn.jpg", "m" : "Cnb.jpg", "M" : "Cnn.jpg",
                             "b" : "Abb.jpg", "B" : "Abn.jpg", "v" : "Anb.jpg", "V" : "Ann.jpg",
                             "q" : "Dbb.jpg", "Q" : "Dbn.jpg", "w" : "Dnb.jpg", "W" : "Dnn.jpg",
                             "k" : "Rbb.jpg", "K" : "Rbn.jpg", "l" : "Rnb.jpg", "L" : "Rnn.jpg",
                             "p" : "Pbb.jpg", "P" : "Pbn.jpg", "o" : "Pnb.jpg", "O" : "Pnn.jpg",
                             " " : "b.jpg", "+" : "n.jpg"}

        self.vertilcal_inicial = "$"
        self.vertilcal_final = "%"

    def guarda(self, board, path):
        file = open(path, "w")
        print(file)
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
            if (i > -1 and i < 8):
                for c in linea:
                    if (c == '$' or c == '%' or c == '\n' or c == '!' or c == '\"' or c == '#'):
                        print("no se lee")
                    else :
                        coordenada = "(" + str(i) + "," + str(j) + ")"
                        try:
                            piece = self.board_pieces[c]
                            board[coordenada] = piece
                            j = j + 1
                        except KeyError as e:
                            board = {}
                            return board
                        except:
                            board = {}
                            return board
            i = i +1
            j = 0
        file.close()
        return board

    #for name, age in mydict.items():
    #   if age == search_age:
    #       print name