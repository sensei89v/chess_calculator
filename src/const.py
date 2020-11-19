import enum


@enum.unique
class FigureType(enum.Enum):
    queen = enum.auto()
    bishop = enum.auto()
    knight = enum.auto()
    rook = enum.auto()
