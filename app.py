from flask import Flask, render_template
from flask_restful import Api
from controllers.usuarios import RegistroController, LoginController
from config import validador, conexion
from os import environ
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL')

api = Api(app=app)
validador.init_app(app)
conexion.init_app(app)

conexion.create_all(app=app)


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


api.add_resource(RegistroController, '/registro')
api.add_resource(LoginController, '/login')

if (__name__ == '__main__'):
    app.run(debug=True, port=8080)
