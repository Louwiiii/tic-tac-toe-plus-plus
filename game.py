class Game:
    def __init__(self, id):
        self.id = id
        self.players_ids = []
        self.turn = 0
        self.grid = [[" " for j in range(9)] for i in range(9)]
        self.moves = [[], []]  # Moves of the two players
        self.winner = None

    def play(self, player_number, action):
        if player_number != self.turn:
            return False

        x, y = map(int,action.split())

        if self.grid[y][x] != " ":
            return False

        # Check if the move is in the correct subgrid
        if len(self.moves[(player_number+1)%2]) > 0:
            last_opponent_move = self.moves[(player_number + 1) % 2][-1]
            subgrid_to_play = (last_opponent_move[0] % 3, last_opponent_move[1] % 3)
            subgrid_played = (x//3, y//3)

            if subgrid_played != subgrid_to_play:
                return False

        self.grid[y][x] = str(player_number)
        self.moves[player_number].append((x, y))
        self.turn = (self.turn+1) % 2

        return True