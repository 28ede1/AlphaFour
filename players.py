import random
from connectfour import check_win_conditions, game_is_over, get_open_slot_index, play_move

def random_player_fn(board, player):
    num_cols = 7
    valid_moves = [i for i in range(num_cols) if board[i] == 0]
    if len(valid_moves) == 0:
        return None
    else:
        return random.choice(valid_moves)

def human_player_fn(board, player):
    """"
    Given a board and a player, retrieve user input of what column to drop a game piece into.

    Args: 
        board (list[int]): list of board positions with 0s, 1s, 2s
        player (int): represents the player (1 or 2)
    Return:
        int represent what column to drop a game piece into, and None if there are no valid moves.
    """
    num_cols = 7
    valid_moves = [i for i in range(num_cols) if board[i] == 0]
    if len(valid_moves) == 0:
        return None
    
    move = input("Enter column (0-6): ")
    
    # handles edge case user input
    try: 
        move = int(move)
    except:
        move = -1

    while move not in valid_moves:
        move = input("Invalid move. Enter column (0-6): ")
        try: 
            move = int(move)
        except:
            move = -1

    return move
    

def evaluation_function(board, player):
    """
    Given a board and a player, return a score representing how favorable the current board state is for the given player.

    Args: 
        board (list[int]): list of board positions with 0s, 1s, 2s
        player (int): represents the player (1 or 2)
    Return:
        Return integer representing score of the board state
    """
    game_win_result = check_win_conditions(board)
    board_is_full = 0 not in {board[i] for i in range(7)} # assumes gravity rules for dropping game pieces are obeyed
    opposing_player = 2 if player == 1 else 1
    if game_win_result == player:
        return 10000000000
    elif game_win_result != 0:
        return -10000000000
    elif board_is_full:
        return 0
        
    board_score = 0

    # consider center column advantage (more possible ways to get 4 in a row available). 
    # positive center_count value indicates player has center advantage, negative means opponent has advantage

    center_count = 0
    center_index = 38
    for i in range(7):
        if board[center_index] == player:
            center_count += 1
        elif board[center_index] != 0:
            center_count -= 1
        center_index -= 7

    board_score += center_count * 5

    # consider the number of columns where you have 3, 2, or just 1 of the same color in column, seperately
    # add negative weightings for the opposing player to get the ai to play more defensively
    board_score += count_n_in_a_column_threats(board, player, 3) * 8
    board_score -= count_n_in_a_column_threats(board, opposing_player, 3) * 8.4

    # consider the number of columns where you have 2 in a column (less threatening then 3 in a row)

    board_score += count_n_in_a_column_threats(board, player, 2) * 4
    board_score -= count_n_in_a_column_threats(board, opposing_player, 2) * 4.4

    # consider just having 1 in a row (even less threatening)

    board_score += count_n_in_a_column_threats(board, player, 1) * 2
    board_score -= count_n_in_a_column_threats(board, opposing_player, 1) * 2.4
    return board_score

def count_n_in_a_column_threats(board, player, target_chain_length):
    """
    Given a board, a player, and a target_chain_length,
    count the number of columns where the player has exactly N consecutive pieces
    stacked vertically (such that the player could potential play another piece in that column)

    Args: 
        board (list[int]): list of board positions with 0s, 1s, 2s
        player (int): represents the player (1 or 2)
        target_chain_length (int): represents the column type to look for
    Return:
       Return interger represent the number of columns that the player has N pieces in a column
    """
    column_start_index = 0
    n_way_count = 0
    for i in range(7):
        current_index = column_start_index

        # skip full columns 
        if board[current_index] != 0:
            column_start_index += 1
            continue
        
        # once a non-full column is found, go the the topmost piece that is not 0
        chain_count = 0
        while current_index <= 41 and board[current_index] == 0:
            current_index += 7

        # keep counting if you have several game pieces of the same color in a column
        while current_index <= 41 and board[current_index] == player:
            chain_count += 1
            current_index += 7
            
        if chain_count == target_chain_length:
            n_way_count += 1

        column_start_index += 1
    return n_way_count

def minimax(board, eval_fn, whose_turn, who_am_i, num_plys):

    def alpha_beta_minimax(board, eval_fn, whose_turn, who_am_i, num_plys, alpha=float("-inf"), beta=float("inf")):
        """
        runs minimax with alpha-beta pruning to evaluate a game state.

        Simulates alternating turns up to a given depth given by num_plays.
    
        Args:
            board (list[int]): list of board positions with 0s, 1s, 2s
            eval_fn (method): method that is used to evaluate the goodness of a state
            whose_turn (int): integer determining who is maximizing or minimizing
            who_am_i (int): represents the player to score the board in reference to
            num_plys (int): provides depth to search to
            alpha (float): initialized to -inf, the best score that MAX (who_am_i) can gaurentee
            beta (float): initialized to inf, the worst score that MAX (who_am_i) can gaurentee the opponent will force onto them
        """
        if (num_plys <= 0) or game_is_over(board):
            return eval_fn(board, who_am_i)

        valid_moves = [i for i in range(7) if board[i] == 0]
        opposing_player = 2 if whose_turn == 1 else 1
        best_value = float("-inf") if whose_turn == who_am_i else float("inf")

        for move in valid_moves:
            if alpha >= beta:
                return best_value
            
            # create board copy to prevent child nodes using mutated parent boards
            new_board = board.copy()
            play_move(new_board, whose_turn, move)

            child_value = alpha_beta_minimax(new_board, eval_fn, opposing_player, who_am_i, num_plys - 1, alpha, beta)
            
            if whose_turn == who_am_i:
                best_value = max(best_value, child_value)
                alpha = max(alpha, child_value)
            else:
                best_value = min(best_value, child_value)
                beta = min(beta, child_value)

        return best_value
    
    best_value = float("-inf")
    best_moves = []

    valid_moves = [i for i in range(7) if board[i] == 0]
    opposing_player = 2 if whose_turn == 1 else 1
    
    for move in valid_moves:
         
        # create board copy to prevent child nodes using mutated parent boards
        new_board = board.copy()
        play_move(new_board, whose_turn, move)
        current_minimax_value = alpha_beta_minimax(new_board, eval_fn, opposing_player, who_am_i, num_plys - 1)

        if current_minimax_value == best_value:
            best_moves.append(move)
        elif current_minimax_value > best_value:
            best_value = current_minimax_value
            best_moves = [move]

    return (best_value, best_moves)

    
def initialize_my_player_fn(num_plys=4):
    
    def my_player_fn(board, player):
        """
        Create player_fn that choose the best next move to make for player out of all immediate possible moves.

        Args: 
            board (list[int]): list of board positions with 0s, 1s, 2s
            player (int): represents the player (1 or 2)
        Return:
            Return integer representing column to drop the next game piece into 

        """
        num_cols = 7
        valid_moves = [i for i in range(num_cols) if board[i] == 0]
        if len(valid_moves) == 0:
            return None

        best_value, best_moves = minimax(board, evaluation_function, player, player, num_plys)
        if len(best_moves) == 0:
            return None
        else:
            return random.choice(best_moves)
    return my_player_fn

def initialize_my_player_fn_with_playbook(playbook={}, num_plys=4):
    
    def my_player_fn(board, player):
        """
        Create player_fn that choose the best next move to make for player out of all immediate possible moves.
        Adds board state along with best moves evaluated when called to a playbook dictionary.

        Args: 
            board (list[int]): list of board positions with 0s, 1s, 2s
            player (int): represents the player (1 or 2)
        Return:
            Return integer representing column to drop the next game piece into 

        """
        num_cols = 7
        valid_moves = [i for i in range(num_cols) if board[i] == 0]
        if len(valid_moves) == 0:
            return None

        # memoize 
        if board in playbook:
            best_moves = playbook[board]
        else:
            best_value, best_moves = minimax(board, evaluation_function, player, player, num_plys)
            playbook[tuple(board)] = best_moves

        if len(best_moves) == 0:
            return None
        else:
            return random.choice(best_moves)
    return my_player_fn