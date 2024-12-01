from advent_of_code.two_four.one import calculate_locations_distance, \
    calculate_locations_similarity


def test_calculate_locations_distance(day_1_ids):
    list_a = day_1_ids[0]
    list_b = day_1_ids[1]

    assert calculate_locations_distance(list_a, list_b) == 11


def test_calculate_locations_similarity(day_1_ids):
    list_a = day_1_ids[0]
    list_b = day_1_ids[1]

    assert calculate_locations_similarity(list_a, list_b) == 31
