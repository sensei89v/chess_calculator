from marshmallow import Schema, fields, validate

from .const import FigureType


class InputSchema(Schema):
    n = fields.Integer(validate=validate.Range(min=1, max=8))
    chessPiece = fields.String(validate=validate.OneOf([x.name for x in FigureType]))
