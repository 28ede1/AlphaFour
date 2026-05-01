
import torch

def convert_board_state_to_vector(board, next_move):
    """
    Given a board and a proposed next move, 
    convert the board into a feature vector of length 134 where:
    
    Element 0 (bias) always have a value of 1
    Elements 1-7 represent the proposed move (all except k+1 should be 0, where k is the proposed move)
    Elements 8-141 are triples (a, b, c) corresponding to each cell of the current connect four board where

    a is 1 if the cell is empty else a is 0, 
    b is 1 if the cell contains a red checker else b is 0, and 
    c is 1 if the cell contains a yellow checker (else c is 0)

    Args: 
        board (list[int]): list of board positions with 0s, 1s, 2s of length 42
        player (int): represents the column (0-6) of the board to make a move
    Return:
        returns torch tensor representing the feature vector
    """
    result = torch.zeros(134)
    result[0] = 1.0 # bias
    result[1 + next_move] = 1.0 # proposed_move

    # logic for cell 1 - cell 9
    # Apart from element 0 and elements 1-7, the 
    # remaining elements should represent tuples corresponding to each cell of the connect four board where 
    start_index = 8
    for i in range(42): 
        if board[i] == 0:
            result[start_index] = 1.0
        elif board[i] == 1:
            result[start_index + 1] = 1.0
        else:
            result[start_index + 2] = 1.0
        start_index += 3
    return result


def load_training_data(playbook):
    """
    Given a playbook,
    return a matrix feature vector representation as well an output vector.

    For every board state in the playbook dictionary, for each column in the board state that is not full, 
    create a feature vector of size 134.

    For every board state in the playbook dictionary, for each column in the board that that is not full, 
    add a value of 1.0 to the outcome vector if that board + move combo is optimal, and 0.0 if not.


    Args: 
        playbook (dict[tuple[int], list[int]]):
            Mapping from a flattened 6x7 board state (length 42 tuple)
            to a list of optimal column moves (0–6).

    Return:
        x (torch.Tensor): Feature matrix of shape (N, 134)
        y (torch.Tensor): Binary labels of shape (N,)
            where N = total number of legal moves across all states
    """
    result_x = []
    result_y = []

    for board in playbook:
        for i in range(7):
            if board[i] == 0:
                feature_vector = convert_board_state_to_vector(board, i).tolist()
                result_x.append(feature_vector)

                if i in playbook[board]:
                    result_y.append(1.0)
                else:
                    result_y.append(0.0)

    result_y = torch.tensor(result_y)
    result_x = torch.tensor(result_x)
    return result_x, result_y


# def initialize_params(input_dim=37, hidden_dim=64):
#     theta1 = torch.zeros(hidden_dim, input_dim)
#     theta2 = torch.zeros(hidden_dim, hidden_dim)
#     theta3 = torch.zeros(1, hidden_dim)
#     for theta in [theta1, theta2, theta3]:
#         theta.uniform_(-0.4, 0.4)
#         theta.requires_grad = True
#     return {"theta1": theta1, "theta2": theta2, "theta3": theta3}

# def run_neural_net(parameters, x):
#     theta1 = parameters["theta1"]
#     theta2 = parameters["theta2"]
#     theta3 = parameters["theta3"]
    
#     x = x.transpose(0, 1)
#     z = theta1 @ x
#     stage_1_vector = torch.maximum(torch.zeros(z.shape[0], 1), z)

#     z_2 = theta2 @ stage_1_vector
#     stage_2_vector = torch.maximum(torch.zeros(z_2.shape[0], 1), z_2)

#     z_3 = theta3 @ stage_2_vector
#     return torch.sigmoid(z_3).flatten() # remove the extra dimension

# def compute_loss(output, y):
#     loss = -1 * torch.log(y*output +(1-y)*(1-output))
#     return torch.mean(loss)

# def evaluate_neural_net(parameters, x, y):
#     accuracy = compute_nn_accuracy(parameters, x, y)
#     ai_player_fn = create_nn_player_fn(parameters)
#     wins, losses, ties = play_tournament(50, ai_player_fn, optimal_player_fn)
#     accuracy_msg = f"Train accuracy: {accuracy: .3f}"
#     tournament_msg = f"Tournament performance: {wins}-{losses}-{ties}"
#     print(accuracy_msg + "; " + tournament_msg)

# def compute_nn_accuracy(parameters, x, y):
#     raise NotImplementedError("compute_nn_accuracy has not yet been implemented")


# def create_nn_player_fn(parameters):
#     raise NotImplementedError("create_nn_player_fn has not yet been implemented")


# def train_model(num_steps=100000, learning_rate=0.02, batch_size=128):
#     X_train, y_train = load_training_data(compile_playbook())
#     parameters = initialize_params()
#     batch_start = 0
#     for step in range(num_steps):
#         if step % 5000 == 0:  # we evaluate every 5000 steps
#             evaluate_neural_net(parameters, X_train, y_train)
#         X_batch = X_train[batch_start : batch_start + batch_size, :]
#         y_batch = y_train[batch_start : batch_start + batch_size]
#         output = run_neural_net(parameters, X_batch)
#         loss = compute_loss(output, y_batch)
#         loss.backward()
#         with torch.no_grad():
#             for theta in parameters.values():
#                 theta -= learning_rate * theta.grad
#                 theta.grad = None
#         batch_start = (batch_start + batch_size) % X_train.shape[0]


# if __name__ == "__main__":
#     train_model()