from advent_of_code.two_four.five import sum_middle_value_of_valid_rows, \
    ingest_print_queue, sum_middle_value_of_invalid_rows


def test_ingest_print_queue(day_5_print_queue):
    assert ingest_print_queue(day_5_print_queue) == (
        [
            [47, 53],
            [97, 13],
            [97, 61],
            [97, 47],
            [75, 29],
            [61, 13],
            [75, 53],
            [29, 13],
            [97, 29],
            [53, 29],
            [61, 53],
            [97, 53],
            [61, 29],
            [47, 13],
            [75, 47],
            [97, 75],
            [47, 61],
            [75, 61],
            [47, 29],
            [75, 13],
            [53, 13]
        ],
        [
            [75, 47, 61, 53, 29],
            [97, 61, 53, 29, 13],
            [75, 29, 13],
            [75, 97, 47, 61, 53],
            [61, 13, 29],
            [97, 13, 75, 29, 47],
        ]
    )
    
    
def test_sum_middle_value_of_valid_rows(day_5_print_queue):
    assert sum_middle_value_of_valid_rows(day_5_print_queue) == 143


def test_sum_middle_value_of_invalid_rows(day_5_print_queue):
    assert sum_middle_value_of_invalid_rows(day_5_print_queue) == 123