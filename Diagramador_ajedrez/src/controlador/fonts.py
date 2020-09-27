class Fonst():
    def __init__(self):
        self.path = "partida_merida.txt"
        #self.font = font
        self.merida_pieces = {"Tn" : "R", "Tb" : "r", "tn" : "t", "tb" : "T",
                              "Cn" : "N", "Cn" : "n", "cn" : "M", "cb" : "m",
                              "An" : "B", "Ab" : "b", "an" : "V", "ab" : "v",
                              "Dn" : "Q", "Db" : "q", "dn" : "W", "db" : "w",
                              "Rn" : "k", "Rb" : "K", "rn" : "L", "rb" : "l",
                              "Pn" : "P", "Pb" : "p", "pn" : "O", "pb" : "o",
                              "CASILLA" : " ", "casilla" : "+"}

        self.merida_board =  {"9" : "!\"\"\"\"\"\"\"\"#", "0" : "/(((((((()"}
        self.vertilcal_inicial = "$"
        self.vertilcal_final = "%"
        self.tablero = {"8" : "tMvWLVmT", "7" : "OoOoOoOo", "6" : " + + + +",
                        "5" : "+ + + + ", "4" : " + + + +", "3" : "+ + + + ",
                        "2" : "pPpPpPpP", "1" : "RnBqKbNr"}

    def guarda(self):
            file = open(self.path, "w")
            print(file)
            file.write(self.merida_board["9"])
            file.write("\n")
            for linea in self.tablero:
                row = self.vertilcal_inicial + self.tablero[linea] + self.vertilcal_final
                file.write(row)
                file.write("\n")
            file.write(self.merida_board["0"])
            file.close()
        #self.dim_casilla = 40
        #self.color_casillas = "white"f

Fonst().guarda()