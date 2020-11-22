import pytest

from src.figures import Queen, Knight, Bishop, Rook


@pytest.mark.parametrize('coord, board_size, available_result',
    [
        ((3, 3), 8, [(1, 2), (2, 1), (4, 5), (5, 4), (4, 1), (5, 2), (1, 4), (2, 5)]),
        ((0, 0), 8, [(1, 2), (2, 1)]),
        ((6, 7), 8, [(4, 6), (5, 5), (7, 5)]),
        ((0, 0), 1, []),
        ((1, 1), 3, []),
    ],
)
def test_knight_attacked(coord, board_size, available_result):
    result = Knight.calculate_attacked_positions(coord, board_size)
    assert set(available_result) == set(result)


@pytest.mark.parametrize('coord, board_size, available_result',
    [
        ((3, 3), 8, [(0, 3), (1, 3), (2, 3), (4, 3), (5, 3), (6, 3), (7, 3),
                     (3, 0), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (3, 7)]),
        ((0, 0), 8, [(1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                     (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7)]),
        ((6, 7), 8, [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (7, 7),
                     (6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6)]),
        ((0, 0), 1, []),
        ((1, 1), 3, [(1, 0), (0, 1), (1, 2), (2, 1)]),
    ],
)
def test_rook_attacked(coord, board_size, available_result):
    result = Rook.calculate_attacked_positions(coord, board_size)
    assert set(available_result) == set(result)


@pytest.mark.parametrize('coord, board_size, available_result',
    [
        ((3, 3), 8, [(0, 0), (1, 1), (2, 2), (4, 4), (5, 5), (6, 6), (7, 7),
                     (4, 2), (5, 1), (6, 0), (2, 4), (1, 5), (0, 6)]),
        ((0, 0), 8, [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7)]),
        ((6, 7), 8, [(5, 6), (4, 5), (3, 4), (2, 3), (1, 2), (0, 1), (7, 6)]),
        ((0, 0), 1, []),
        ((1, 1), 3, [(0, 0), (0, 2), (2, 0), (2, 2)]),
    ],
)
def test_bishop_attacked(coord, board_size, available_result):
    result = Bishop.calculate_attacked_positions(coord, board_size)
    assert set(available_result) == set(result)


@pytest.mark.parametrize('coord, board_size, available_result',
    [
        ((3, 3), 8, [(0, 0), (1, 1), (2, 2), (4, 4), (5, 5), (6, 6), (7, 7),
                     (4, 2), (5, 1), (6, 0), (2, 4), (1, 5), (0, 6),
                     (0, 3), (1, 3), (2, 3), (4, 3), (5, 3), (6, 3), (7, 3),
                     (3, 0), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (3, 7)]),
        ((0, 0), 8, [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7),
                     (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                     (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7)]),
        ((6, 7), 8, [(5, 6), (4, 5), (3, 4), (2, 3), (1, 2), (0, 1), (7, 6),
                     (0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (7, 7),
                     (6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6)]),
        ((0, 0), 1, []),
        ((1, 1), 3, [(0, 0), (0, 2), (2, 0), (2, 2), (1, 0), (0, 1), (1, 2), (2, 1)]),
    ],
)
def test_queen_attacked(coord, board_size, available_result):
    result = Queen.calculate_attacked_positions(coord, board_size)
    assert set(available_result) == set(result)
