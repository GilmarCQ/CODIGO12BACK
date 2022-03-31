from models.categorias import Categoria
from config import conexion
from sqlalchemy import or_

def categoriaSeed():
    categorias = conexion.session.query(Categoria).filter(
        or_(
            Categoria.nombre=='OCIO',
            Categoria.nombre=='COMIDA',
            Categoria.nombre=='EDUCACION',
            Categoria.nombre=='VIAJES'
        )).first()
    if categorias is None:
        nombres = ['OCIO', 'COMIDA', 'EDUCACION', 'VIAJES']
        try:
            for categoria in nombres:
                nuevaCategoria = Categoria(nombre=categoria)
                conexion.session.add(nuevaCategoria)
            conexion.session.commit()
            print('Categorias creadas exitosamente')
        except Exception as e:
            conexion.session.rollback()
            print('Error al alimentar la BD')


