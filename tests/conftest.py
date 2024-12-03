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