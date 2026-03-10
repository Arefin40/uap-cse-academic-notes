class TicTacToe:
    WIN_COMBINATIONS = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6],             # diagonals
    ]

    def __init__(self, maximizer="X", minimizer="O"):
        self.board = [" "] * 9
        self.maximizer = maximizer
        self.minimizer = minimizer

    def display(self):
        b = self.board
        print(f" {b[0]} | {b[1]} | {b[2]} ")
        print("---+---+---")
        print(f" {b[3]} | {b[4]} | {b[5]} ")
        print("---+---+---")
        print(f" {b[6]} | {b[7]} | {b[8]} \n")

    def game_over(self):
        for a, b, c in self.WIN_COMBINATIONS:
            if self.board[a] == self.board[b] == self.board[c] != " ":
                return 1 if self.board[a] == self.maximizer else -1
        if " " not in self.board:
            return 0
        return None

    def available_moves(self):
        return [i for i, v in enumerate(self.board) if v == " "]

    def minimax(self, maximizing_player=True, depth=0, alpha=float("-inf"), beta=float("inf")):
        result = self.game_over()

        if result is not None:
            return result, None

        best_move = None

        if maximizing_player:
            max_score = float("-inf")

            for move in self.available_moves():
                self.board[move] = self.maximizer
                score, _ = self.minimax(False, depth + 1, alpha, beta)
                self.board[move] = " "

                if score > max_score:
                    max_score = score
                    best_move = move

                alpha = max(alpha, score)
                if beta <= alpha:
                    break
            return max_score, best_move
        else:
            min_score = float("inf")

            for move in self.available_moves():
                self.board[move] = self.minimizer
                score, _ = self.minimax(True, depth + 1, alpha, beta)
                self.board[move] = " "
                if score < min_score:
                    min_score = score
                    best_move = move
                beta = min(beta, score)
                if beta <= alpha:
                    break

            return min_score, best_move


if __name__ == "__main__":
    game = TicTacToe()
    print()

    game.board[0] = game.board[2] = game.board[5] = "X"
    game.board[1] = game.board[3] = game.board[4] = "O"
    game.display()

    best_score, best_move = game.minimax()
    print("Best score for X:", best_score)
    print("Best move for X:", best_move)
