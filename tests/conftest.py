import pytest


@pytest.fixture
def day_1_ids():
    return [
        [3, 4, 2, 1, 3, 3],
        [4, 3, 5, 3, 9, 3],
    ]


@pytest.fixture
def day_2_levels():
    return """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""


@pytest.fixture
def day_3_corrupted_muls():
    return "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"


@pytest.fixture
def day_3_conditioned_muls():
    return "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"