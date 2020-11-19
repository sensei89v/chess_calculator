from flask import Flask, request

from .calculation import calculate
from .const import FigureType


app = Flask(__name__)


@app.route('/', methods=['POST'])
def hello_world():
    input_data = request.get_json()
    board_size = input_data['n']       # TODO: add good validation
    figure_type_str = input_data['chessPiece']
    figure_type = FigureType[figure_type_str]
    soultion_count = calculate(figure_type, board_size, board_size)
    return {"solutionsCount": soultion_count}


if __name__ == '__main__':
    app.run(port=8000)
