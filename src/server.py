from flask import Flask, request
import json
from werkzeug.exceptions import HTTPException

from .calculation import calculate
from .const import FigureType
from .schemas import InputSchema


app = Flask(__name__)


@app.errorhandler(HTTPException)
def handle_flask_exception(e):
    response = e.get_response()
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response

# Todo: upgrade error handler
@app.errorhandler(Exception)
def handle_common_exception(e):
    response = json.dumps({
        "code": 400,
        "name": 'Something wrong',
        "description": str(e),
    })
    return response, 400


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
