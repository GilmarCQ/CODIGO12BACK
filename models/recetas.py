from config import conexion
from sqlalchemy import Column, types


class Receta(conexion.Model):
    pass
    id = Column(type_=types.Integer, autoincrement=True, primary_key=True)
    nombre = Column(type_=types.String(45), nullable=False)
    duracion = Column(type_=types.String(45))
    comensales = Column(type_=types.Integer, nullable=False)
    estado = Column(type_=types.Boolean, default=True)
    dificultad = Column(type_=types.Enum('FACIL', 'INTERMEDIO', 'DIFICIL', 'EXTREMO'), default='FACIL')
    __tablename__ = 'recetas'
