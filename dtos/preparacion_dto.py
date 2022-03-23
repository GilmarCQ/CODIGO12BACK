from config import validador
from models.preparaciones import Preparacion
from marshmallow_sqlalchemy import fields
from models.recetas import Receta


class PreparacionRequestDTO(validador.SQLAlchemyAutoSchema):
    class Meta:
        model = Preparacion
        # para validar en el DTO la validacion, se tiene que agregar el atributo include_fk y asi se realize
        # las validaciones respectivas
        include_fk = True

class RecetaResponseDTO(validador.SQLAlchemyAutoSchema):
    class Meta:
        model=Receta

class PreparacionResponseDTO(validador.SQLAlchemyAutoSchema):
    receta = fields.Nested(nested=RecetaResponseDTO, data_key='receta_relacion')
    class Meta:
        model = Preparacion
        # cargara las instancias asociadas a la preparacion (Relaciones)
        load_instance = True
        include_fk = True
        include_relationship = True
