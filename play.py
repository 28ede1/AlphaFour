from connectfour import check_win_conditions
from connectfour import play_move
from connectfour import print_board
from players import random_player_fn, initialize_my_player_fn, human_player_fn
import sys
import time
from tqdm import tqdm


def play_game(player1_fn, player2_fn, min_delay=0.2, visualize=True):
    """
        Play a single game of connect four using the two player functions.
        Displays board state in terminal each round.

        Args: 
            player1_fn : function that determines what move player 1 should make
            player2_fn : function that determines what move player 2 should make
            min_delay (float): delay used for the visualization
            visualize (boolean): whether or not the game should be visualized in terminal
        Return:
            Return integer representing who the winner of the game is 
    """
    def clear_screen():
        # Clear screen and move cursor to (0,0)
        sys.stdout.write("\033[2J\033[H")
        sys.stdout.flush()

    num_rows, num_cols = 6, 7
    board = [0 for _ in range(num_rows * num_cols)]
    moves_made = 0
    current_player = 1
    while check_win_conditions(board) == 0 and moves_made < 42:
        if visualize:
            clear_screen()
            print_board(board)
            print(f"\nplayer {current_player} is thinking...")
        player_fn = player1_fn if current_player == 1 else player2_fn
        start = time.time()
        col = player_fn(board, current_player) # optimal move should be replaced here
        if visualize:
            elapsed = time.time() - start
            if elapsed < min_delay:
                time.sleep(min_delay - elapsed)
        play_move(board, current_player, col)
        current_player = 2 if current_player == 1 else 1
        moves_made += 1
    winner = check_win_conditions(board)
    if visualize:
        clear_screen()
        print_board(board)
        if winner == 0:
            print("\ntie!")
        else:
            print(f"\nwinner is player {winner}!")
    return winner


def play_tournament(player1_fn, player2_fn, num_rounds):
    """
        Plays a tournament between player 1 and player 2 for some number of rounds.
        In each round, two games are player, one whether player 1 is the first player to make a move, 
        and another where player 2 is the first player. This ensures fairness w respect to turn order.

        The result of the number of rounds * 2 is printed in string format.
        Args: 
            player1_fn : function that determines what move player 1 should make
            player2_fn : function that determines what move player 2 should make
            num_rounds (int): number of rounds to play

    """
    p1_wins, p2_wins, ties = 0, 0, 0
    for _ in tqdm(range(num_rounds)):
        winner = play_game(player1_fn, player2_fn, visualize=False)
        if winner == 0:
            ties += 1
        elif winner == 1:
            p1_wins += 1
        elif winner == 2:
            p2_wins += 1
        winner = play_game(player2_fn, player1_fn, visualize=False)
        if winner == 0:
            ties += 1
        elif winner == 1:
            p2_wins += 1
        elif winner == 2:
            p1_wins += 1
    print(f"P1-P2-T: {p1_wins}-{p2_wins}-{ties}")


if __name__ == "__main__":
    # play_game(random_player_fn, random_player_fn)
    ai_player_fn = initialize_my_player_fn()
    play_game(ai_player_fn, human_player_fn)

    # play_tournament(ai_player_fn, random_player_fn, 100)