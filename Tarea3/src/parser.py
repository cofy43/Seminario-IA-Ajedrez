class Parser():
    def __init__(self, paht):
        self.path = paht
        self.moves = []
        self.games = []
        self.n_games = 0
        self.result = ''
        self.read_file()
        self.generate_games()

    def clean_comments(self, line):

        if line.startswith("["):
            if line.startswith("[Event"):
                self.n_games += 1

            line = line.replace("\n", "")
            self.moves.append(line)

        else :
            ini_comment = line.find('{')
            fin_comment = line.find('}')
            if ini_comment > 0:
                line = line[: ini_comment] + line[fin_comment+1 :]
            clean = line.split(" ")
            for item in clean:
                item = item.replace("\n", "")
                if item and (item.find('...') < 0):
                    self.moves.append(item)


    def read_file(self):
        archivo = open(self.path,'r', encoding='utf-8', errors='ignore')
        lista = archivo.readlines()

        for line in lista:
            self.clean_comments(line)
            # incrementa en 1 el contador  
            # muestra contador y elemento (línea)
        
        archivo.close()  # cierra archivo

    def generate_games(self):
        game = []
        for elem in self.moves:
            if elem.startswith("[Result"):
                ini = elem.find('\"')
                self.result = elem[ini+1 : len(elem)-2]
                
            game.append(elem)
            
            if elem == self.result:
                self.games.append(game)
                game = []

        for j in self.games:
            print(j, "\n\n\n")


if __name__ == "__main__":
    parser = Parser('nuevo-london.pgn')
    pass