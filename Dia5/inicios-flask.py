from flask import Flask
from datetime import datetime

# __name__  >   muestra si el archivo es el archivo raiz o principal del proyecto, si es el archivo principal, en ese
# caso el valor de __name__ sera __main__ ya que se estara en el archivo principal de mi proyecto
app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hola mundo</h1>'

@app.route('/api/info')
def info_app():
    return {
        'fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }

# app.run   >   inicializa nuestro servidor
app.run(debug=True)
