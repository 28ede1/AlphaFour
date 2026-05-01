from play import *
from players import *
import json

def create_training_data_file():
    pb = {}
    ai_player_fn_2 = initialize_my_player_fn_with_playbook(pb, 6)
    
    play_tournament(ai_player_fn_2, ai_player_fn_2, 300)
    play_tournament(random_player_fn, ai_player_fn_2, 300)
    play_tournament(ai_player_fn_2, random_player_fn, 300)
    
    with open("training_data/training.json", 'w') as writer:
        json.dump(list(pb.items()), writer)

def compile_playbook():
    pb = {}
    with open("training_data/training.json") as reader:
        data = json.load(reader)
    
    for entry in data:
        key = tuple(entry[0])
        pb[key] = entry[1]
    return pb

if __name__ == "__main__":
    create_training_data_file()
    # compile_playbook()