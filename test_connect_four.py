from connectfour import *
from players import count_n_in_a_column_threats, count_immediate_future_wins

# test args

test_board_1 = [
    0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,
    0,0,0,0,0,0,0
]

test_board_2 = [
    0,0,2,0,0,0,0,
    0,0,1,0,0,0,0,
    0,0,2,0,0,0,0,
    0,0,1,0,0,0,0,
    0,0,2,0,0,0,0,
    0,0,1,0,0,0,0
]

test_board_3 = [
    0,0,0,0,0,0,0,
    0,0,0,2,0,0,0,
    0,1,0,1,0,0,0,
    2,2,1,2,0,0,0,
    1,1,2,1,0,0,0,
    2,2,1,2,1,0,0
]

test_board_4 = [
    0,0,0,0,0,0,0,
    1,0,0,0,0,0,0,
    2,0,0,0,0,0,0,
    1,0,2,0,0,0,0,
    2,0,1,0,0,0,0,
    1,2,2,0,0,0,0
]

test_board_5 = [
    0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,
    0,0,2,0,0,0,0,
    0,0,1,0,0,0,0,
    0,0,2,0,0,0,0,
    0,0,1,0,0,0,0
]

test_board_6 = [
    0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,
    1,1,1,1,0,0,0
]

test_board_7= [
    0,0,0,0,0,0,0,
    0,0,2,0,0,0,0,
    0,0,2,0,0,0,0,
    0,0,2,0,0,0,0,
    0,0,2,0,0,0,0,
    1,1,1,0,0,0,0
]

test_board_8 = [
    1,2,1,2,1,2,1,
    2,1,2,1,2,1,2,
    1,2,1,2,1,2,1,
    2,1,2,1,2,1,2,
    1,2,1,2,1,2,1,
    2,1,2,1,2,1,2
]

test_board_9 = [
    0,0,0,0,0,0,0,
    0,0,0,1,0,0,0,
    0,0,1,2,0,0,0,
    0,1,2,2,0,0,0,
    1,2,2,2,0,0,0,
    2,1,1,1,0,0,0
]   

test_board_10 = [
    0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,
    2,1,0,0,0,0,0,
    2,2,1,0,0,0,0,
    2,2,2,1,0,0,0,
    1,1,1,2,0,0,0
]

test_board_11 = [
    0,0,0,0,0,0,0,
    0,0,0,0,0,2,0,
    0,0,1,1,0,1,0,
    0,1,2,1,1,2,0,
    1,1,1,2,2,1,0,
    2,1,2,1,1,2,2
]

test_board_12 = [
    0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,
    0,0,0,1,0,0,0,
    0,0,0,1,0,0,0,
    0,0,0,1,0,0,0,
    0,2,0,2,0,0,0
]

test_board_13 = [
    0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,
    0,1,0,1,0,0,0,
    0,1,0,1,0,0,0,
    0,1,0,1,0,0,0,
    2,2,2,2,0,0,0
]

test_board_14 = [
    0,0,0,0,0,0,0,
    0,0,2,0,0,0,0,
    0,1,1,1,0,0,0,
    0,1,1,1,0,0,0,
    0,1,1,1,0,0,0,
    2,2,2,2,0,0,0
]

test_board_15 = [
    0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,
    0,1,1,1,0,0,0,
    0,1,1,1,0,0,0,
    0,1,1,1,0,0,0,
    2,2,2,2,0,0,0
]

test_board_16 = [
    0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,
    0,2,0,0,0,0,0,
    0,2,0,2,0,0,0,
    1,2,1,2,0,0,0,
    1,1,1,2,0,0,1
]

test_board_17 = [
    0,0,0,1,0,0,0,
    0,0,0,1,0,0,0,
    0,0,0,1,0,0,0,
    0,0,0,2,0,0,0,
    0,0,0,2,0,0,0,
    2,2,0,2,0,0,0
]

test_board_18 = [
    0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,
    0,1,0,2,0,0,0,
    0,1,0,2,0,0,0,
    2,2,1,1,0,0,0
]

test_board_19 = [
    0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,
    0,0,0,1,0,0,0,
    0,0,0,1,0,0,0,
    2,2,0,2,0,0,0
]

test_board_20 = [
    0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,
    0,1,0,0,0,0,0,
    0,1,0,1,0,0,0,
    0,1,0,1,0,0,0,
    2,2,0,2,0,0,0
]

test_board_21 = [
    0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,
    1,0,0,0,2,0,0,
    1,2,2,0,2,2,2,
    1,1,1,0,2,2,2
]

test_board_22 = [
    0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,
    0,1,0,1,0,0,0,
    0,1,0,1,0,0,0,
    1,1,0,1,0,0,0
]


test_board_24 = [
    0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,
    0,0,2,0,0,0,0,
    0,1,2,0,0,0,0,
    1,1,2,0,0,0,0,
    1,1,1,0,2,2,2
]

test_board_25 = [
    0,0,0,0,0,0,0,
    2,0,0,0,0,0,0,
    2,1,2,0,0,0,0,
    1,2,2,0,0,0,0,
    1,2,2,0,0,0,0,
    1,1,1,0,2,2,2
]

def test_get_open_slot_index():

    # Test that for an empty board, all dropped game pieces should end up on the last row
    # Test that for an full board, None is always returned (indicated that the column to drop a piece into is full)
    current_open_slot_index = 35
    for i in range(7):
        assert get_open_slot_index(test_board_1, i) == current_open_slot_index
        assert get_open_slot_index(test_board_8, i) == None
        current_open_slot_index += 1

    assert get_open_slot_index(test_board_3, 0) == 14
    assert get_open_slot_index(test_board_4, 1) == 29
    assert get_open_slot_index(test_board_5, 2) == 9
    assert get_open_slot_index(test_board_2, 2) == None

def test_play_move():
    final_state_1 = [
        0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,
        0,0,0,0,0,1,0
    ]

    final_state_2 = [
        0,0,0,1,0,0,0,
        0,0,0,2,0,0,0,
        0,1,0,1,0,0,0,
        2,2,1,2,0,0,0,
        1,1,2,1,0,0,0,
        2,2,1,2,1,0,0
    ]
    final_state_3 = [
        0,0,0,0,0,0,0,
        0,0,2,0,0,0,0,
        0,0,2,0,0,0,0,
        0,0,1,0,0,0,0,
        0,0,2,0,0,0,0,
        0,0,1,0,0,0,0
    ]

    assert play_move(list(test_board_1), 1, 5) == final_state_1
    assert play_move(list(test_board_3), 1, 3) == final_state_2
    assert play_move(list(test_board_5), 2, 2) == final_state_3

def test_column_win_conditions():
    assert check_col_conditions(test_board_7, 2) == True
    assert check_col_conditions(test_board_7, 1) == False

    assert check_col_conditions(test_board_8, 2) == False
    assert check_col_conditions(test_board_8, 1) == False

def test_row_win_conditions():

    assert check_row_conditions(test_board_6, 1) == True
    assert check_row_conditions(test_board_6, 2) == False

    assert check_row_conditions(test_board_8, 2) == False
    assert check_row_conditions(test_board_8, 1) == False

def test_diagonal_win_conditions():

    assert check_diagonal_conditions(test_board_9, 1) == True
    assert check_diagonal_conditions(test_board_9, 2) == True

    assert check_diagonal_conditions(test_board_10, 1) == False
    assert check_diagonal_conditions(test_board_10, 2) == True

    assert check_diagonal_conditions(test_board_7, 1) == False
    assert check_diagonal_conditions(test_board_7, 2) == False


def test_three_way_threat_count():
    assert count_n_in_a_column_threats(test_board_12, 2, 3) == 0
    assert count_n_in_a_column_threats(test_board_12, 1, 3) == 1
    assert count_n_in_a_column_threats(test_board_3, 1, 3) == 0
    assert count_n_in_a_column_threats(test_board_13, 1, 3) == 2
    assert count_n_in_a_column_threats(test_board_14, 1, 3) == 2
    assert count_n_in_a_column_threats(test_board_15, 1, 3) == 3
    assert count_n_in_a_column_threats(test_board_16, 2, 3) == 2
    assert count_n_in_a_column_threats(test_board_16, 1, 3) == 0
    assert count_n_in_a_column_threats(test_board_17, 1, 3) == 0
    assert count_n_in_a_column_threats(test_board_18, 1, 3) == 0
    assert count_n_in_a_column_threats(test_board_22, 1, 3) == 2

def test_two_way_threat_count():
    assert count_n_in_a_column_threats(test_board_12, 2, 2) == 0
    assert count_n_in_a_column_threats(test_board_12, 1, 2) == 0
    assert count_n_in_a_column_threats(test_board_3, 1, 2) == 0
    assert count_n_in_a_column_threats(test_board_13, 1, 2) == 0
    assert count_n_in_a_column_threats(test_board_14, 1, 2) == 0
    assert count_n_in_a_column_threats(test_board_15, 1, 2) == 0
    assert count_n_in_a_column_threats(test_board_16, 1, 2) == 2
    assert count_n_in_a_column_threats(test_board_16, 2, 2) == 0
    assert count_n_in_a_column_threats(test_board_17, 1, 2) == 0
    assert count_n_in_a_column_threats(test_board_18, 1, 2) == 1
    assert count_n_in_a_column_threats(test_board_18, 2, 2) == 1
    assert count_n_in_a_column_threats(test_board_19, 1, 2) == 1
    assert count_n_in_a_column_threats(test_board_20, 1, 2) == 1
    assert count_n_in_a_column_threats(test_board_22, 1, 2) == 0

def test_one_way_threat_count():
    assert count_n_in_a_column_threats(test_board_12, 2, 1) == 1
    assert count_n_in_a_column_threats(test_board_12, 1, 1) == 0
    assert count_n_in_a_column_threats(test_board_3, 1, 1) == 3
    assert count_n_in_a_column_threats(test_board_13, 1, 1) == 0
    assert count_n_in_a_column_threats(test_board_14, 1, 1) == 0
    assert count_n_in_a_column_threats(test_board_15, 2, 1) == 1
    assert count_n_in_a_column_threats(test_board_16, 1, 1) == 1
    assert count_n_in_a_column_threats(test_board_16, 2, 1) == 0
    assert count_n_in_a_column_threats(test_board_17, 2, 1) == 2
    assert count_n_in_a_column_threats(test_board_18, 1, 1) == 1
    assert count_n_in_a_column_threats(test_board_18, 2, 1) == 1
    assert count_n_in_a_column_threats(test_board_19, 2, 1) == 2
    assert count_n_in_a_column_threats(test_board_20, 1, 1) == 0
    assert count_n_in_a_column_threats(test_board_22, 1, 1) == 1

def test_immediate_future_win_count():
    assert count_immediate_future_wins(test_board_11, 1, 2) == (4,0)
    assert count_immediate_future_wins(test_board_19, 1, 2) == (0,1)
    assert count_immediate_future_wins(test_board_24, 1, 2) == (2,2)
    assert count_immediate_future_wins(test_board_25, 1, 2) == (1,2)
    assert count_immediate_future_wins(test_board_8, 1, 2) == (0,0)


if __name__ == "__main__":
    test_get_open_slot_index()
    print('get_open_slot_index functions correctly! ✅')

    test_play_move()
    print('play_move functions correctly! ✅')

    test_column_win_conditions()
    print('column_win_conditions functions correctly! ✅')

    test_row_win_conditions()
    print('row_win_conditions functions correctly! ✅')

    test_diagonal_win_conditions()
    print('diagonal_win_conditions functions correctly! ✅')

    test_three_way_threat_count()
    print('count_n_in_a_row_threats functions correctly! (three-way threats) ✅')

    test_two_way_threat_count()
    print('count_n_in_a_row_threats functions correctly! (two-way threats) ✅')

    test_one_way_threat_count()
    print('count_n_in_a_row_threats functions correctly! (one-way threats) ✅')

    test_immediate_future_win_count()
    print('count_immediate_future_wins functions correctly! ✅')