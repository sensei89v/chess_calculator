from .const import FigureType


class Figure:
    @staticmethod
    def calculate_attacked_positions(coord, board_size):
        return {}


class Rook(Figure):
    @staticmethod
    def calculate_attacked_positions(coord, board_size):
        x, y = coord
        return {(i, y) for i in range(0, board_size) if i != x} | {(x, i) for i in range(0, board_size) if i != y}

class Bishop(Figure):
    @staticmethod
    def calculate_attacked_positions(coord, board_size):
        x, y = coord
        return {(x + i, y + i) for i in range(-board_size, board_size) if (i != 0 and 0 <= (x + i) < board_size and 0 <= (y + i) < board_size)} | \
               {(x - i, y + i) for i in range(-board_size, board_size) if (i != 0 and 0 <= (x - i) < board_size and 0 <= (y + i) < board_size)}

class Queen(Figure):
    @staticmethod
    def calculate_attacked_positions(coord, board_size):
        # TODO: apply inheritence
        attacked = Rook.calculate_attacked_positions(coord, board_size)
        attacked |= Bishop.calculate_attacked_positions(coord, board_size)
        return attacked


class Knight(Figure):
    @staticmethod
    def calculate_attacked_positions(coord, board_size):
        x, y = coord
        candidates = [
            (x + 2, y + 1),
            (x + 1, y + 2),
            (x - 2, y + 1),
            (x - 1, y + 2),
            (x + 2, y - 1),
            (x + 1, y - 2),
            (x - 2, y - 1),
            (x - 1, y - 2)
        ]
        return {(i_x, i_y) for i_x, i_y in candidates if 0 <= i_x < board_size and 0 <= i_y < board_size}


def get_figure_class_by_figure_type(figure_type):
    _map = {
        FigureType.bishop: Bishop,
        FigureType.queen: Queen,
        FigureType.knight: Knight,
        FigureType.rook: Rook
    }
    return _map.get(figure_type)
