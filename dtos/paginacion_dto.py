from config import validador
from marshmallow import fields


class PaginacionRequestDTO(validador.Schema):
    page = fields.Integer(required=False, load_default=1, min=1)
    perPage = fields.Integer(required=False, load_default=10, min=1)
