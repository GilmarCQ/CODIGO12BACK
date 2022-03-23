from flask_restful import Resource, request
from config import conexion
from models.recetas import Receta
from dtos.receta_dto import (RecetaRequestDTO,
                             RecetaResponseDTO,
                             BuscarRecetaRequestDTO,
                             RecetaPreparacionesRespondeDTO)
from dtos.paginacion_dto import PaginacionRequestDTO
from math import ceil


# CREATE, GET ALL (PAGINATED), UPDATED, FIND por like de nombre, DELETE
class RecetasController(Resource):
    def post(self):
        body = request.get_json()
        try:
            data = RecetaRequestDTO().load(body)
            print(data)
            nuevaReceta = Receta(
                nombre=data.get('nombre'),
                duracion=data.get('duracion'),
                comensales=data.get('comensales'),
                estado=data.get('estado'),
                dificultad=data.get('dificultad')
            )
            conexion.session.add(nuevaReceta)
            conexion.session.commit()
            contenido = RecetaRequestDTO().dump(nuevaReceta)
            return {
                       'message': 'Receta creada correctamente',
                       'receta': contenido
                   }, 201
            pass
        except Exception as e:
            conexion.session.rollback()
            return {
                'message': 'Error al crear la receta',
                'content': e.args
            }

    def get(self):
        query_params = request.args
        paginacion = PaginacionRequestDTO().load(query_params)
        perPage = paginacion.get('perPage')
        page = paginacion.get('page')
        if (page < 1 or perPage < 1):
            return {
                       'message': 'Los parametros no pueden recibir parametros negativos.'
                   }, 400
        skip = perPage * (page - 1)
        recetas = conexion.session.query(Receta).limit(perPage).offset(skip).all()
        total = conexion.session.query(Receta).count()
        itemsPerPage = perPage if total >= perPage else total
        totalPages = ceil(total / itemsPerPage) if itemsPerPage > 0 else None
        prevPage = page - 1 if page > 1 and page <= totalPages else None
        nextPage = page + 1 if totalPages > 1 and page < totalPages else None

        respuesta = RecetaResponseDTO(many=True).dump(recetas)
        return {
            'message': "Consulta Exitosa",
            'paginacion': total,
            'itemsPerPage': itemsPerPage,
            'totalPages': totalPages,
            'contenido': respuesta,
            'prevPage': prevPage,
            'nextPage': nextPage
        }


class BuscarRecetaController(Resource):
    def get(self):
        query_params = request.args
        try:
            params = BuscarRecetaRequestDTO().load(query_params)

            # si es que no me dan a buscar el nombre entonces hare la buscqueda de todas las recetas
            # el filter a comparacion del filter_by se utiliza para comparar valores pero usando el atributo de la
            # clase y se usa doble igual
            # si queremos usar algun filtro en especifico del orm (de la bd) entonces usaremos el atributo de la
            # clase el cual nos devolvera metodos para hacer esa busqueda especifica
            # recetas2 = conexion.session.query(Receta).filter(Receta.nombre.like('%fajo%')).filter_by(estado=True).all()
            # print(recetas2)

            nombre = params.get('nombre', '')
            if params.get('nombre') is not None:
                del params['nombre']

            recetas = conexion.session.query(Receta).filter(Receta.nombre.like('%{}%'.format(nombre))).filter_by(
                **params).all()
            respuesta = RecetaResponseDTO(many=True).dump(recetas)

            return {
                'message': '',
                'contenido': respuesta
            }
        except Exception as e:
            return {
                       'message': 'Ha ocurrido un error en la consulta',
                       'content': e.args
                   }, 400


class RecetaController(Resource):
    def get(self, id):
        # buscar receta segun ID
        # si no hay la receta devolcer un mensaje: 'Receta no encontrada' con un estado not found
        receta: Receta | None = conexion.session.query(Receta).filter(Receta.id == id).first()
        if receta is not None:
            print(receta.preparaciones)
            respuesta = RecetaPreparacionesRespondeDTO().dump(receta)
            return {
                       'message': 'Receta encontrada',
                       'content': respuesta
                   }, 201
        else:
            return {
                       'message': 'Receta no encontrada'
                   }, 404
        # conexion.session.
