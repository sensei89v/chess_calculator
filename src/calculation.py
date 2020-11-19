from .figures import get_figure_class_by_figure_type


def _build_board(board_size):
    return {(x, y) for x in range(board_size) for y in range(board_size)}


def _run_calculation(figure_class, board, board_size, figure_count):
    result = 0

    if figure_count == 0:
        return 1

    while figure_count <= len(board):
        coord = board.pop()

        attacked_coords = figure_class.calculate_attacked_positions(coord, board_size)
        new_board = board.copy() - set(attacked_coords)
        result += _run_calculation(figure_class, new_board, board_size, figure_count - 1)

    return result


def calculate(figure_type, board_size, figure_count):
    if board_size <= 0:
        return 0

    figure_class = get_figure_class_by_figure_type(figure_type)

    if figure_class is None:
        raise ValueError("Incorrect figure")

    board = _build_board(board_size)
    return _run_calculation(figure_class, board, board_size, figure_count)
