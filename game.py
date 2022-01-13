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

        subgrid_played = (x // 3, y // 3)

        # Check if the move is in the correct subgrid
        if len(self.moves[(player_number+1)%2]) > 0:
            last_opponent_move = self.moves[(player_number + 1) % 2][-1]
            subgrid_to_play = (last_opponent_move[0] % 3, last_opponent_move[1] % 3)

            if subgrid_played != subgrid_to_play and not self.subgrid_finished(subgrid_to_play):
                return False

        self.grid[y][x] = str(player_number)
        self.moves[player_number].append((x, y))
        self.turn = (self.turn+1) % 2

        #verifier si la sous grille est gagné ou pas
        if self.subgrid_finished(subgrid_played):
            for i in range(subgrid_played[1]*3,(subgrid_played[1]*3)+3):
                for j in range(subgrid_played[0]*3,(subgrid_played[0]*3)+3):
                    self.grid[i][j] = str(player_number)

        global_grid = [[" " for j in range(3)] for i in range(3)]

        for i in range(3):
            for j in range(3):
                winner = self.get_winner(self.get_subgrid((j, i)))
                global_grid[i][j] = str(winner) if winner is not None and winner!=-1 else " "

        self.winner = self.get_winner(global_grid)

        if self.winner is not None:
            self.turn = -1

        return True

    def subgrid_finished(self, subgrid_pos):
        subgrid = self.get_subgrid(subgrid_pos)
        return self.get_winner(subgrid) is not None

    def get_subgrid(self, pos):
        x, y = pos
        subgrid = []
        for i in range(y * 3, (y * 3) + 3):
            subgrid.append(self.grid[i][x*3:x*3+3])

        return subgrid

    def get_winner(self, subgrid):
        """

        :param subgrid: 3x3 subgrid to check
        :return: winner number, -1 if it's a tie or None if grid is not finished
        """
        lines = [subgrid[i] for i in range(3)]
        columns = [[subgrid[i][j] for i in range(3)] for j in range(3)]
        diagonals = [[subgrid[i][i] for i in range(3)]] + [[subgrid[i][2 - i] for i in range(3)]]
        triplets = lines + columns + diagonals
        filled = True
        for triplet in triplets:
            element = triplet[0]
            if triplet.count(" ") != 0:
                filled = False
            if triplet.count(element) == 3 and element != " ":
                return int(element)
        if filled:
            return -1
        return None



