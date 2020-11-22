from flask import Flask, request, jsonify
import json
from werkzeug.exceptions import HTTPException
from marshmallow import ValidationError

from .calculation import calculate
from .const import FigureType
from .schemas import InputSchema


app = Flask(__name__)


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


@app.route('/', methods=['POST'])
def chess_calulator():
    input_data = request.get_json()
    params = InputSchema().load(input_data)

    board_size = params['n']
    figure_type_str = params['chessPiece']
    figure_type = FigureType[figure_type_str]

    soultion_count = calculate(figure_type, board_size, board_size)
    return {"solutionsCount": soultion_count}


if __name__ == '__main__':
    app.run()
