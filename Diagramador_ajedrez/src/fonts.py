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