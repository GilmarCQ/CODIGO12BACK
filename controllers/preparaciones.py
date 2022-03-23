from config import conexion
from flask_restful import Resource, request
from models.preparaciones import Preparacion
from dtos.preparacion_dto import PreparacionRequestDTO, PreparacionResponseDTO


class PreparacionesController(Resource):
    def post(self):
        try:
            body = request.get_json()
            print(body)
            data = PreparacionRequestDTO().load(body)
            nuevaPreparacion = Preparacion(**data)
            conexion.session.add(nuevaPreparacion)
            conexion.session.commit()
            respuesta = PreparacionResponseDTO().dump(nuevaPreparacion)

            return {
                       'message': 'Preparacion creada correctamente.',
                       'content': respuesta
                   }, 201
        except Exception as e:
            conexion.session.rollback()
            return {
                       'message': 'Hubo un error al crear la poreparacion.',
                       'content': e.args
                   }, 400

    def get(self):
        preparacion:Preparacion | None = conexion.session.query(Preparacion).filter_by(id=1).first()
        print(preparacion)
        print(preparacion.orden)
        # ahora desde la preparacion podemos ingresar mediante su relationship al registro al cula pertenece esta
        # preparacion y luego a los atributos de esa tabla
        print(preparacion.receta.nombre)
        print(preparacion.receta_id)
        return {
            'message': 'Ok'
        }
