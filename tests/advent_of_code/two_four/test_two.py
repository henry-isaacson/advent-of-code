from advent_of_code.two_four.two import levels_to_2d, count_safe_levels, \
    count_safe_levels_with_dampener


def test_levels_to_2d(day_2_levels):
    assert levels_to_2d(day_2_levels) == [
        [7, 6, 4, 2, 1],
        [1, 2, 7, 8, 9],
        [9, 7, 6, 2, 1],
        [1, 3, 2, 4, 5],
        [8, 6, 4, 4, 1],
        [1, 3, 6, 7, 9],
    ]


def test_count_safe_levels(day_2_levels):
    assert count_safe_levels(day_2_levels) == 2


def test_count_safe_levels_with_dampener(day_2_levels):
    assert count_safe_levels_with_dampener(day_2_levels) == 4