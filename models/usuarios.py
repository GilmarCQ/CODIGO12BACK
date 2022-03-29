from config import conexion
from sqlalchemy import Column, types
from bcrypt import hashpw, gensalt


class Usuario(conexion.Model):
    __tablename__ = 'usuario'
    id = Column(type_=types.Integer, primary_key=True, autoincrement=True)
    nombre = Column(type_=types.String(length=45))
    apellidos = Column(type_=types.String(length=45))
    correo = Column(type_=types.String(length=45), unique=True, nullable=False)
    password = Column(type_=types.Text(), nullable=False)

    def encriptar_pwd(self):
        password_bytes = bytes(self.password, 'utf-8')
        salt = gensalt(rounds=10)
        hash_password = hashpw(password_bytes, salt)
        # convertir a formato string para guardar en la base de datos
        hash_pwd_string = hash_password.decode('utf-8')
        self.password = hash_pwd_string