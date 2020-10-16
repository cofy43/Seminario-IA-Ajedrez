class Game():

    def __init__(self, game):

        self.header = {
            'event' : None, 
            'site' : None, 
            'date' : None, 
            'round' : None, 
            'white' : None, 
            'black' : None, 
            'result' : None,
        }

        self.moves = []
        self.game = game
        self.text_game = ''
        self.build_game()
    
    def build_game(self):
        temp = ''
        for item in self.game:
            if item.startswith("["):
                self.set_header(item)
            else:
                self.moves.append(item)
                self.text_game += item + " "


    def set_header(self, header):
        ini = header.find("\"")
        value = header[ini+1 : len(header)-2]
        key = header[1:ini-1]
        self.header[key.lower()] = value