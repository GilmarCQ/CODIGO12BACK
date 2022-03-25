from config import conexion
from sqlalchemy import Column, types


class Usuario(conexion.Model):
    __tablename__ = 'usuario'
    id = Column(type_=types.Integer, primary_key=True, autoincrement=True)
    nombre = Column(type_=types.String(length=45))
    apellidos = Column(type_=types.String(length=45))
    correo = Column(type_=types.String(length=45), unique=True, nullable=False)
    password = Column(type_=types.Text(), nullable=False)
