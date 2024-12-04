from advent_of_code.two_four.three import sum_uncorrupted_muls, \
    sum_muls_with_conditional


def test_sum_uncorrupted_muls(day_3_corrupted_muls):
    assert sum_uncorrupted_muls(day_3_corrupted_muls) == 161


def test_sum_muls_with_conditional(day_3_conditioned_muls):
    assert sum_muls_with_conditional(day_3_conditioned_muls) == 48