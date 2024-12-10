from advent_of_code.two_four.six import count_guard_positions, map_to_2d


def test_count_guard_positions(day_6_map):
    assert count_guard_positions(day_6_map) == 41
