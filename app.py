from flask import Flask, render_template, request
from flask_restful import Api
from controllers.usuarios import (RegistroController, LoginController, ResetPasswordController)
from config import validador, conexion
from os import environ
from dotenv import load_dotenv
from flask_cors import CORS
from flask_jwt import JWT, jwt_required, current_identity
from seguridad import autenticador, identificador
from datetime import timedelta
from dtos.registro_dto import UsuarioResponseDto
from seed import categoriaSeed
from controllers.movimientos import MovimientosController
from cryptography.fernet import Fernet
from datetime import datetime
from models.usuarios import Usuario
import json

load_dotenv()

app = Flask(__name__)

CORS(app=app)

app.config['SECRET_KEY'] = environ.get('JWT_SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL')
# pewrmite cambiar el endpoint de jwt
app.config['JWT_AUTH_URL_RULE'] = '/login-jwt'
# cambia la llave para solicitar el username
app.config['JWT_AUTH_USERNAME_KEY'] = 'correo'
# cambia la llave para solicitar el password
app.config['JWT_AUTH_PASSWORD_KEY'] = 'pass'
app.config['JWT_EXPIRATION_DELTA'] = timedelta(hours=1, minutes=5)
# Permite configurar cual sera el prefijo del token en los headers de autorizacion
app.config['JWT_AUTH_HEADER_PREFIX'] = 'Bearer'

jsonwebtoken = JWT(app=app, authentication_handler=autenticador, identity_handler=identificador)

api = Api(app=app)
validador.init_app(app)
conexion.init_app(app)

conexion.create_all(app=app)


@app.before_first_request
def seed():
    print('haciendo el seed')
    categoriaSeed()


@app.route('/')
def inicio():
    # return 'no hay nada'
    return render_template('inicio.jinja', nombre='Gilmar', dis='Jueves',
                           integrantes=[
                               'Foca',
                               'Lapagol',
                               'Ruidiaz',
                               'Paolin',
                               'El Rasho'
                           ],
                           usuario={
                               'nombre': 'Juan',
                               'direccion': 'Las Piedritas',
                               'edad': '40'
                           },
                           selecciones=[
                               {
                                   'nombre': 'Bolivia',
                                   'clasificado': False
                               },
                               {
                                   'nombre': 'Brasil',
                                   'clasificado': True
                               }
                           ])


@app.route('/yo')
@jwt_required()
def perfil_usuario():
    print(current_identity)
    contenido = UsuarioResponseDto().dump(current_identity)
    return {
        'message': 'El usuario es',
        'content': contenido
    }


@app.route('/validar-token', methods=['POST'])
def validar_token():
    body = request.get_json()
    token = body.get('token')
    fernet = Fernet(environ.get('FERNET_SECRET_KEY'))
    try:
        # el metodo decrypt se usa para descifrar la token previamente encryptada, de ser incorrecta se lanzara un error
        # la token la convierto a bytes y luego el resultado lo convertimos a string
        data = fernet.decrypt(bytes(token, 'utf-8')).decode('utf-8')
        print(data)
        diccionario = json.loads(data)
        fecha_caducidad = datetime.strptime(diccionario.get('fecha_caducidad'), '%Y-%m-%d %H:%M:%S.%f')
        hora_actual = datetime.now()
        if hora_actual <= fecha_caducidad:
            # with_entities >   permitira elegir las columnas que desea consultar
            usuarioEncontrado = conexion.session.query(Usuario).with_entities(Usuario.correo).filter_by(
                id=diccionario.get('id_usuario')).first()
            if usuarioEncontrado:
                return {
                       'message': 'Si es el usuario',
                       'correo': usuarioEncontrado.correo
                   }, 200
            else:
                return {
                    'message': 'Usuario no existe'
                }, 400
        else:
            return {
                       'message': 'El token ha vencido'
                   }, 200
    except Exception as e:
        return {
                   'message': 'Token incorrecto'
               }, 400


api.add_resource(RegistroController, '/registro')
api.add_resource(LoginController, '/login')
api.add_resource(ResetPasswordController, '/reset-password')
api.add_resource(MovimientosController, '/movimiento', '/movimientos')

if (__name__ == '__main__'):
    app.run(debug=True, port=8080)
