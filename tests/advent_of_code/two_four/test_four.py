from advent_of_code.two_four.four import solve_xmas_wordsearch, \
    wordsearch_to_2d, solve_x_mas_wordsearch


def test_wordsearch_to_2d(day_4_wordsearch):
    assert wordsearch_to_2d(day_4_wordsearch) == [
        ["M", "M", "M", "S", "X", "X", "M", "A", "S", "M"],
        ["M", "S", "A", "M", "X", "M", "S", "M", "S", "A"],
        ["A", "M", "X", "S", "X", "M", "A", "A", "M", "M"],
        ["M", "S", "A", "M", "A", "S", "M", "S", "M", "X"],
        ["X", "M", "A", "S", "A", "M", "X", "A", "M", "M"],
        ["X", "X", "A", "M", "M", "X", "X", "A", "M", "A"],
        ["S", "M", "S", "M", "S", "A", "S", "X", "S", "S"],
        ["S", "A", "X", "A", "M", "A", "S", "A", "A", "A"],
        ["M", "A", "M", "M", "M", "X", "M", "M", "M", "M"],
        ["M", "X", "M", "X", "A", "X", "M", "A", "S", "X"],
    ]


def test_solve_xmas_wordsearch(day_4_wordsearch):
    assert solve_xmas_wordsearch(day_4_wordsearch) == 18

def test_solve_x_mas_wordsearch(day_4_wordsearch):
    assert solve_x_mas_wordsearch(day_4_wordsearch) == 9