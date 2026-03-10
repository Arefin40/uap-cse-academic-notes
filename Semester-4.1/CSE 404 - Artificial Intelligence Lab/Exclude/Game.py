class TicTocToe:
    WIN_MASKS = [
        0b111000000,
        0b000111000,
        0b000000111,  # row
        0b100100100,
        0b010010010,
        0b001001001,  # column
        0b100010001,
        0b001010100,  # diagonal
    ]

    def __init__(self, board_size=3, player_X="X", player_O="O", empty=" ", game_mode="Human"):
        self.BOARD_SIZE = board_size
        self.PLAYER_X = player_X
        self.PLAYER_O = player_O
        self.EMPTY = empty
        self.GAME_MODE = game_mode

        # initial state
        self.x_mask = self.y_mask = 0b0
        self.MOVES_COUNT = 0
        self.PLAYER = self.PLAYER_X
        self.BOARD = [[self.EMPTY] * self.BOARD_SIZE] * self.BOARD_SIZE

    def display(self):
        print("\n--+---+--\n".join(" | ".join(row) for row in self.BOARD))

    def get_opponent(self):
        return self.PLAYER_O if self.PLAYER == self.PLAYER_X else self.PLAYER_X

    def get_available_moves(self, x_mask, o_mask):
        occupied = x_mask | o_mask
        return [i for i in range(9) if not (occupied & (1 << (8 - i)))]

    def is_game_over(self, x_mask, o_mask):
        for mask in TicTocToe.WIN_MASKS:
            if (x_mask & mask) == mask:
                return f"{self.PLAYER_X} wins 🎉"
            if (o_mask & mask) == mask:
                return f"{self.PLAYER_O} wins 🎉"

        if (x_mask | o_mask) == 0b111111111:
            return "Draw"

        return None

    def minmax(self, board, depth, alpha, beta, maximizing_player):
        pass


if __name__ == "__main__":
    game = TicTocToe()
    game.display()
    print(game.WIN_MASKS)
    # state = [["O", "X", "X"], ["O", "O", "X"], ["X", "O", "O"]]
    # state[1].append("= 6")
    # game.display(state)
