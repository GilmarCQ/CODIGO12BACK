from flask import Flask, render_template

app = Flask(__name__)


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


if (__name__ == '__main__'):
    app.run(debug=True)
