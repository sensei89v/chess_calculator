from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException
from marshmallow import ValidationError

from .calculation import calculate_variant_count
from .const import FigureType
from .schemas import InputSchema


app = Flask(__name__)


# ######### error handling
def _create_error_response(name, description='', code=500):
    """
    Common error function
    """
    response = {
        "code": code,
        "name": name,
        "description": description
    }
    return jsonify(response), code


@app.errorhandler(HTTPException)
def handle_flask_exception(exception):
    return _create_error_response(exception.name, exception.description, exception.code)


@app.errorhandler(ValidationError)
def handle_validation_exception(exception):
    return _create_error_response("Incorrect input data", str(exception), 400)


@app.errorhandler(Exception)
def handle_common_exception(exception):
    return _create_error_response("internal exception", str(exception), 500)


# ######### routing
@app.route('/', methods=['POST'])
def chess_calulator():
    input_data = request.get_json()
    params = InputSchema().load(input_data)

    board_size = params['n']
    figure_type_str = params['chessPiece']
    figure_type = FigureType[figure_type_str]

    soultion_count = calculate_variant_count(figure_type, board_size, board_size)
    return {"solutionsCount": soultion_count}


@app.route('/quick', methods=['POST'])
def quick_chess_calulator():
    input_data = request.get_json()
    params = InputSchema().load(input_data)

    board_size = params['n']
    figure_type_str = params['chessPiece']
    figure_type = FigureType[figure_type_str]

    # We can using precalculated values becouse we have only 4 * 8 == 32 cases
    # WARNING!!! If you change calculate_variant_count, please change precalulated values
    _response_map = {
        (FigureType.queen, 1): 1,
        (FigureType.queen, 2): 0,
        (FigureType.queen, 3): 0,
        (FigureType.queen, 4): 2,
        (FigureType.queen, 5): 10,
        (FigureType.queen, 6): 4,
        (FigureType.queen, 7): 40,
        (FigureType.queen, 8): 92,
        (FigureType.knight, 1): 1,
        (FigureType.knight, 2): 6,
        (FigureType.knight, 3): 36,
        (FigureType.knight, 4): 412,
        (FigureType.knight, 5): 9386,
        (FigureType.knight, 6): 257318,
        (FigureType.knight, 7): 8891854,
        (FigureType.knight, 8): 379978716,
        (FigureType.bishop, 1): 1,
        (FigureType.bishop, 2): 4,
        (FigureType.bishop, 3): 26,
        (FigureType.bishop, 4): 260,
        (FigureType.bishop, 5): 3368,
        (FigureType.bishop, 6): 53744,
        (FigureType.bishop, 7): 1022320,
        (FigureType.bishop, 8): 22522960,
        (FigureType.rook, 1): 1,
        (FigureType.rook, 2): 2,
        (FigureType.rook, 3): 6,
        (FigureType.rook, 4): 24,
        (FigureType.rook, 5): 120,
        (FigureType.rook, 6): 720,
        (FigureType.rook, 7): 5040,
        (FigureType.rook, 8): 40320,
    }

    if (figure_type, board_size) in _response_map:
        soultion_count = _response_map[(figure_type, board_size)]
    else:
        soultion_count = calculate_variant_count(figure_type, board_size, board_size)

    return {"solutionsCount": soultion_count}


if __name__ == '__main__':
    app.run()
