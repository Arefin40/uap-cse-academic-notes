import math
import random
import sys
import time

# --- Constants ---
EMPTY = " "
PLAYER_X = "X"
PLAYER_O = "O"
BOARD_SIZE = 3

# --- Utility functions ---


def create_board():
    return [[EMPTY for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]


def print_board(board):
    """Print board to console in a readable form."""
    lines = []
    for r in range(BOARD_SIZE):
        row = " | ".join(board[r])
        lines.append(f" {row} ")
        if r < BOARD_SIZE - 1:
            lines.append("-" * (BOARD_SIZE * 4 - 3))
    print("\n".join(lines))


def available_moves(board):
    """Return list of (r, c) empty positions."""
    moves = []
    for r in range(BOARD_SIZE):
        for c in range(BOARD_SIZE):
            if board[r][c] == EMPTY:
                moves.append((r, c))
    return moves


def get_opponent(player):
    return PLAYER_O if player == PLAYER_X else PLAYER_X


def check_winner(board):
    """Return PLAYER_X or PLAYER_O if someone won; 'D' for draw; None otherwise."""
    lines = []

    # Rows and cols
    for i in range(BOARD_SIZE):
        lines.append(board[i])  # row
        lines.append([board[r][i] for r in range(BOARD_SIZE)])  # col

    # Diagonals
    lines.append([board[i][i] for i in range(BOARD_SIZE)])
    lines.append([board[i][BOARD_SIZE - 1 - i] for i in range(BOARD_SIZE)])

    for line in lines:
        if all(cell == PLAYER_X for cell in line):
            return PLAYER_X
        if all(cell == PLAYER_O for cell in line):
            return PLAYER_O

    if not available_moves(board):
        return "D"  # Draw

    return None  # Game ongoing


def evaluate_board(board, ai_player):
    """Evaluate board for ai_player.
    Returns +10 for ai win, -10 for opponent win, 0 for draw/ongoing.
    Use depth adjustments in minimax to prefer faster wins / slower losses.
    """
    winner = check_winner(board)
    if winner == ai_player:
        return 10
    elif winner == get_opponent(ai_player):
        return -10
    else:
        return 0


# --- Minimax with Alpha-Beta pruning ---


def minimax(board, depth, alpha, beta, maximizing_player, ai_player):
    """
    Depth-limited minimax with alpha-beta.
    - board: current board
    - depth: remaining search depth (int). If depth == 0, evaluate heuristically.
    - alpha, beta: bounds
    - maximizing_player: boolean, True if current node is maximizing for ai_player.
    - ai_player: 'X' or 'O' representing the AI we're optimizing for.
    Returns (best_score, best_move) where best_move is (r,c) or None.
    """
    winner = check_winner(board)
    if winner is not None:
        # Terminal node (win/lose/draw) — immediate evaluation
        score = evaluate_board(board, ai_player)
        return score, None

    if depth == 0:
        # Depth limit reached: use heuristic (here simple evaluation)
        score = evaluate_board(board, ai_player)
        return score, None

    best_move = None
    if maximizing_player:
        max_eval = -math.inf
        for r, c in available_moves(board):
            board[r][c] = ai_player
            eval_score, _ = minimax(board, depth - 1, alpha, beta, False, ai_player)
            # prefer faster wins: no direct depth factor here since we evaluate terminal nodes above.
            board[r][c] = EMPTY

            if eval_score > max_eval:
                max_eval = eval_score
                best_move = (r, c)

            alpha = max(alpha, eval_score)
            if beta <= alpha:
                break  # beta cutoff
        return max_eval, best_move
    else:
        min_eval = math.inf
        opp = get_opponent(ai_player)
        for r, c in available_moves(board):
            board[r][c] = opp
            eval_score, _ = minimax(board, depth - 1, alpha, beta, True, ai_player)
            board[r][c] = EMPTY

            if eval_score < min_eval:
                min_eval = eval_score
                best_move = (r, c)

            beta = min(beta, eval_score)
            if beta <= alpha:
                break  # alpha cutoff
        return min_eval, best_move


def make_ai_move(board, ai_player, search_depth):
    """Choose the best move for ai_player using minimax with alpha-beta."""
    # If board empty, pick center or random to speed up
    moves = available_moves(board)
    if not moves:
        return None

    # Small optimization: if center is available and depth >= 1, pick it
    center = (BOARD_SIZE // 2, BOARD_SIZE // 2)
    if board[center[0]][center[1]] == EMPTY and search_depth >= 1:
        # still run minimax to be consistent, but can prefer center if scores tie
        pass

    score, move = minimax(board, search_depth, -math.inf, math.inf, True, ai_player)
    # If minimax returns None for move (e.g., depth==0), pick random available
    if move is None:
        move = random.choice(moves)
    r, c = move
    board[r][c] = ai_player
    return move


# --- Game loops for modes ---


def human_move(board, human_player):
    """Get valid human move from console."""
    moves = available_moves(board)
    if not moves:
        return None
    while True:
        try:
            user = input("Enter your move as row,col (1-3 each), e.g. 2,3: ").strip()
            if user.lower() in ("q", "quit", "exit"):
                print("Exiting game.")
                sys.exit(0)
            parts = user.split(",")
            if len(parts) != 2:
                raise ValueError
            r = int(parts[0].strip()) - 1
            c = int(parts[1].strip()) - 1
            if (r, c) in moves:
                board[r][c] = human_player
                return (r, c)
            else:
                print("Invalid move or cell occupied. Try again.")
        except (ValueError, IndexError):
            print("Invalid input format. Use row,col numbers 1 to 3.")


def play_human_vs_computer():
    board = create_board()
    print("Choose your symbol: X always goes first.")
    while True:
        choice = input("Play as X or O? (X goes first): ").strip().upper()
        if choice in (PLAYER_X, PLAYER_O):
            human = choice
            break
        else:
            print("Please choose X or O.")

    ai = get_opponent(human)
    # Set AI depth
    while True:
        try:
            depth = int(input("Set AI search depth (1-9). 9 = full depth (optimal): ").strip())
            if 1 <= depth <= 9:
                break
            else:
                print("Enter integer between 1 and 9.")
        except ValueError:
            print("Invalid number.")

    current = PLAYER_X  # X always starts
    print("\nStarting game: Human ({}) vs Computer ({})\n".format(human, ai))
    print_board(board)
    print()

    while True:
        if current == human:
            print(f"Human ({human}) turn.")
            human_move(board, human)
        else:
            print(f"Computer ({ai}) is thinking... (depth={depth})")
            move = make_ai_move(board, ai, depth)
            print(f"Computer played: {move[0] + 1},{move[1] + 1}")

        print_board(board)
        winner = check_winner(board)
        if winner is not None:
            if winner == "D":
                print("Game ended in a draw.")
            else:
                who = "Human" if winner == human else "Computer"
                print(f"{who} ({winner}) wins!")
            break

        current = get_opponent(current)
        print()


def play_computer_vs_computer():
    board = create_board()
    print("Computer vs Computer mode.")

    # Set depths for both AIs
    def get_depth_for(ai_name):
        while True:
            try:
                d = int(input(f"Set search depth for {ai_name} (1-9): ").strip())
                if 1 <= d <= 9:
                    return d
                else:
                    print("Enter integer between 1 and 9.")
            except ValueError:
                print("Invalid number.")

    depth_x = get_depth_for("Computer X")
    depth_o = get_depth_for("Computer O")

    current = PLAYER_X
    print_board(board)
    print()
    time.sleep(0.5)

    while True:
        if current == PLAYER_X:
            print(f"Computer X thinking (depth={depth_x})...")
            make_ai_move(board, PLAYER_X, depth_x)
        else:
            print(f"Computer O thinking (depth={depth_o})...")
            make_ai_move(board, PLAYER_O, depth_o)

        print_board(board)
        winner = check_winner(board)
        if winner is not None:
            if winner == "D":
                print("Game ended in a draw.")
            else:
                print(f"Computer {winner} wins!")
            break

        current = get_opponent(current)
        print()
        time.sleep(0.5)


def main_menu():
    print("=== Tic Tac Toe: Minimax + Alpha-Beta ===")
    while True:
        print("\nSelect mode:")
        print("1) Human vs Computer")
        print("2) Computer vs Computer")
        print("3) Exit")
        choice = input("Enter 1, 2 or 3: ").strip()
        if choice == "1":
            play_human_vs_computer()
        elif choice == "2":
            play_computer_vs_computer()
        elif choice == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\nInterrupted. Exiting.")
