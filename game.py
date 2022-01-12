class Game:
    def __init__(self, id):
        self.id = id
        self.players_ids = []
        self.turn = 0
        self.grid = [[" " for j in range(9)] for i in range(9)]
        self.winner = None

    def play(self, player_number, action):
        pass