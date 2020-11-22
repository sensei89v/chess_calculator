import pytest

from src.const import FigureType
from src.calculation import calculate


@pytest.mark.parametrize('figure_type, board_size, figure_count, available_result',
    [
        (FigureType.queen, 8, 8, 92),
        (FigureType.knight, 3, 3, 36),
        (FigureType.rook, 3, 3, 6),
        (FigureType.bishop, 3, 3, 26),
    ],
)
def test_knight_attacked(figure_type, board_size, figure_count, available_result):
    result = calculate(figure_type, board_size, figure_count)
    assert available_result == result
