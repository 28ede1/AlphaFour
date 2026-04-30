from play import *
from players import *
import json

if __name__ == "__main__":
    # initialize a playbook list of board states found and corresponding best moves and save to json file
    # each element in the list is a list containing the board state (list of length 42) and a list of best moves found (columns to drop a piece in)
    pb = {}
    ai_player_fn_1 = initialize_my_player_fn_with_playbook()
    ai_player_fn_2 = initialize_my_player_fn_with_playbook(pb, 5)
    
    play_tournament(ai_player_fn_1, ai_player_fn_2, 500)
    play_tournament(ai_player_fn_2, ai_player_fn_1, 500)
    play_tournament(random_player_fn, ai_player_fn_2, 500)
    play_tournament(ai_player_fn_2, random_player_fn, 500)
    
    with open("training.json", 'w') as writer:
        json.dump(list(pb.items()), writer)

    