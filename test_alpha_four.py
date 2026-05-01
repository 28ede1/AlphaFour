from alphafour import *

test_board_1 = [
    0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,
    0,0,0,0,0,0,0
]

test_board_2 = [
    1,1,1,1,1,1,1,
    1,1,1,1,1,1,1,
    1,1,1,1,1,1,1,
    1,1,1,1,1,1,1,
    1,1,1,1,1,1,1,
    1,1,1,1,1,1,1
]

test_board_3 = [
    2,2,2,2,2,2,2,
    2,2,2,2,2,2,2,
    2,2,2,2,2,2,2,
    2,2,2,2,2,2,2,
    2,2,2,2,2,2,2,
    2,2,2,2,2,2,2
]

test_board_4 = [
    0,0,1,0,2,0,0,
    0,2,1,0,2,0,0,
    1,2,2,1,1,0,0,
    2,1,1,2,2,1,0,
    1,2,2,1,1,2,0,
    2,1,1,2,2,1,0
]

def test_convert_board_state_to_vector():
    expected_result_board_1_feature_vector = torch.tensor([1] + [1, 0, 0, 0, 0, 0, 0] + [1, 0, 0] * 42)
    move_test_1 = 0

    assert torch.equal(expected_result_board_1_feature_vector, convert_board_state_to_vector(test_board_1, move_test_1))

    expected_result_board_2_feature_vector = torch.tensor([1] + [0, 0, 0, 0, 1, 0, 0] + [0, 1, 0] * 42)
    move_test_2 = 4

    assert torch.equal(expected_result_board_2_feature_vector, convert_board_state_to_vector(test_board_2, move_test_2))

    expected_result_board_3_feature_vector = torch.tensor([1] + [0, 1, 0, 0, 0, 0, 0] + [0, 0, 1] * 42)
    move_test_3 = 1

    assert torch.equal(expected_result_board_3_feature_vector, convert_board_state_to_vector(test_board_3, move_test_3))

    [
    0,0,1,0,2,0,0,
    0,2,1,0,2,0,0,
    1,2,2,1,1,0,0,
    2,1,1,2,2,1,0,
    1,2,2,1,1,2,0,
    2,1,1,2,2,1,0
]   
    expected_result_board_4_feature_vector = torch.tensor([1] + [0, 1, 0, 0, 0, 0, 0] + [1,0,0, 1,0,0, 0,1,0, 1,0,0, 0,0,1, 1,0,0, 
    1,0,0, 1,0,0, 0,0,1, 0,1,0, 1,0,0, 0,0,1, 1,0,0, 1,0,0, 0,1,0, 0,0,1, 0,0,1, 0,1,0, 0,1,0, 1,0,0, 1,0,0, 0,0,1, 0,1,0, 
    0,1,0, 0,0,1, 0,0,1, 0,1,0, 1,0,0, 0,1,0, 0,0,1, 0,0,1, 0,1,0, 0,1,0, 0,0,1, 1,0,0, 0,0,1, 0,1,0, 0,1,0, 0,0,1, 0,0,1,
    0,1,0, 1,0,0])

    move_test_4 = 1

    assert torch.equal(expected_result_board_4_feature_vector, convert_board_state_to_vector(test_board_4, move_test_4))

def test_load_training_data():
    pb_1 = {
        (0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,
         0,0,0,0,0,0,0): [3]
    }

    expected_x_1 = torch.tensor([
        [1] + [1, 0, 0, 0, 0, 0, 0] + [1, 0, 0] * 42,
        [1] + [0, 1, 0, 0, 0, 0, 0] + [1, 0, 0] * 42,
        [1] + [0, 0, 1, 0, 0, 0, 0] + [1, 0, 0] * 42,
        [1] + [0, 0, 0, 1, 0, 0, 0] + [1, 0, 0] * 42,
        [1] + [0, 0, 0, 0, 1, 0, 0] + [1, 0, 0] * 42,
        [1] + [0, 0, 0, 0, 0, 1, 0] + [1, 0, 0] * 42,
        [1] + [0, 0, 0, 0, 0, 0, 1] + [1, 0, 0] * 42
    ])

    expected_y_1 = torch.tensor([0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0])

    actual_x_1, actual_y_1 = load_training_data(pb_1)

    assert torch.equal(expected_x_1, actual_x_1)
    assert torch.equal(expected_y_1, actual_y_1)


if __name__ == "__main__":
    test_convert_board_state_to_vector()
    print('convert_board_state_to_vector functions correctly! ✅')

    test_load_training_data()
    print('load_training_data functions correctly! ✅')

    
