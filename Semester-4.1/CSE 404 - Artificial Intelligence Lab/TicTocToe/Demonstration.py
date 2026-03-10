from Game import TicTacToe
import random


def print_menu():
    print("\n=== Tic-Tac-Toe ===")
    print("1. Human vs Human")
    print("2. Human vs AI")
    print("3. AI vs AI")
    print("4. Exit")


def print_cells():
    print(" 1 | 2 | 3 \n---+---+---\n 4 | 5 | 6 \n---+---+---\n 7 | 8 | 9 ")


def get_move_input(prompt, board):
    while True:
        try:
            move = int(input(prompt)) - 1
            if move < 0 or move > 8 or board[move] != " ":
                print("Invalid move. Try again.")
                continue
            return move
        except ValueError:
            print("Invalid input. Please enter a number from 1 to 9.")


def play_turn(game, player, is_ai=False, random_move=False):
    if is_ai:
        if random_move:
            move = random.choice(game.available_moves())
            print(f"AI ({player}) makes a random move at position {move + 1}")
            game.board[move] = player
        else:
            print(f"AI ({player}) is thinking...")
            score, move = game.minimax(maximizing_player=(player == game.maximizer))
            game.board[move] = player
            print(f"AI ({player}) plays at position {move + 1}")
    else:
        move = get_move_input(f"Player {player}, enter your move (1-9): ", game.board)
        game.board[move] = player


def print_result(result, game):
    if result == 1:
        print(f"{game.maximizer} wins!")
    elif result == -1:
        print(f"{game.minimizer} wins!")
    else:
        print("It's a draw!")


def play_game(player_types, ai_vs_ai_first_random=False):
    game = TicTacToe()
    print_cells()
    game.display()
    current = "X"
    move_count = 0

    while True:
        is_ai = player_types[current] == "AI"
        # For AI vs AI, make the very first move random
        random_first_ai_move = ai_vs_ai_first_random and move_count == 0 and is_ai

        play_turn(game, current, is_ai, random_move=random_first_ai_move)
        move_count += 1
        game.display()

        result = game.game_over()
        if result is not None:
            print_result(result, game)
            break

        current = "O" if current == "X" else "X"


def human_vs_human():
    play_game({"X": "Human", "O": "Human"})


def human_vs_ai():
    human = input("Choose your symbol [X/O] (X goes first): ").upper()
    while human not in ["X", "O"]:
        human = input("Invalid input. Choose X or O: ").upper()
    ai = "O" if human == "X" else "X"
    play_game({human: "Human", ai: "AI"})


def ai_vs_ai():
    play_game({"X": "AI", "O": "AI"}, ai_vs_ai_first_random=True)


def play():
    options = {"1": human_vs_human, "2": human_vs_ai, "3": ai_vs_ai, "4": lambda: print("Goodbye!")}
    while True:
        print_menu()
        choice = input("Choose an option (1-4): ")
        if choice in options:
            if choice == "4":
                options[choice]()
                break
            options[choice]()
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    play()
