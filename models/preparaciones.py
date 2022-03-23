from config import conexion
from sqlalchemy import Column, types, orm
from sqlalchemy.sql.schema import ForeignKey


class Preparacion(conexion.Model):
    __tablename__ = 'preparaciones'
    id = Column(type_=types.Integer, primary_key=True, autoincrement=True)
    descripcion = Column(type_=types.String(length=45), nullable=False)
    orden = Column(type_=types.Integer, nullable=False)

    receta_id = Column(ForeignKey(column='recetas.id'), type_=types.Integer)
    # el relationship me sirve para poder navegar desde un modelo hacia el otro, el foreign key solo sirve para que
    # a nivel de base de datos me haga la validacion de la relacion mas no para acceder desde un modelo hacia el otro
    # backref =>    creara un atributo virtual que solamente se podra llamar desde la clase de la cual estamos
    # trabajando
    receta = orm.relationship('Receta', backref='preparaciones')
