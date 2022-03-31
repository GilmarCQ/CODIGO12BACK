from flask_restful import Resource, request
from models.movimientos import Movimiento
from dtos.movimiento_dto import MovimientoRequestDTO, MovimientoResponseDTO
from flask_jwt import jwt_required, current_identity
from config import conexion


class MovimientosController(Resource):
    @jwt_required()
    def post(self):
        body = request.get_json()
        try:
            data = MovimientoRequestDTO().load(body)
            # a la data se le agrega el valor del usuario id en la cual proviene del token JWT
            data['usuario_id'] = current_identity.id
            nuevoMovimiento = Movimiento(**data)
            conexion.session.add(nuevoMovimiento)
            conexion.session.commit()
            contenido = MovimientoResponseDTO().dump(nuevoMovimiento)
            return {
                'message': 'Movimiento creado correctamente',
                'content': contenido
            }
        except Exception as e:
            conexion.session.rollback()
            return {
                'message': 'Error al crear el movimiento',
                'content': e.args
            }

    @jwt_required()
    def get(self):
        movimientos : list[Movimiento] = conexion.session.query(Movimiento).filter_by(usuario_id=current_identity.id).all()
        contenido = MovimientoResponseDTO(many=True).dump(movimientos)
        return {
            'message': 'Consulta exitosa',
            'content': contenido
        }, 200
