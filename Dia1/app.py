from flask import Flask, request
from datetime import datetime
from flask_cors import CORS, cross_origin

app = Flask(__name__)
# si solamente mandamos a llamar a la clase y le pasamos la instancia de la clase Flask, creara los permisos para
# que todos puedan acceder (Allowed-Origin), para que cualquier metodo sea consultado (Allowed-Method) y para que
# cualquier header se pueda permitir (Allowed-Header)
CORS(app=app, origins=['http://localhost:63342'])

clients = [
{
    "id": 1,
    "nombre": "Eduardo",
    "pais": "PERU",
    "edad": 29,
    "organos": True,
    "casado": False
}
]

def find_client(id):
    for position in range(0,len(clients)):
        client = clients[position]
        if client.get('id') == id:
            return client, position

@app.route('/')
def estatus():
    hour_server = datetime.now()
    return {
        'status': True,
        'hour': hour_server.strftime('%Y/%m/%d %H:%M:%S')
    }

@app.route('/clients', methods=['POST', 'GET'])
# cross_origin permite modificar el acceso de reglas CORS para un endpoint en especifico con sus respectivo metodos
@cross_origin(origins=['http://localhost:63342', 'www.mipagina.com'])
def get_clients():
    if request.method == 'POST':
        data = request.get_json()
        data['id'] = len(clients) + 1
        clients.append(data)
        return {
            'message': 'Cliente agregado correctamente',
            'client': data
        }
    elif request.method == 'GET':
        return {
            'message': 'Lista de Clientes',
            'clients': clients
        }

@app.route('/client/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def get_client(id):
    print(request.method)
    if request.method == 'GET':
        client = find_client(id)
        if client:
            return {
                'message': 'Cliente encontrado',
                'client': client[0]
            }
        return {
            'message': 'No se encontro el cliente'
        }, 404
    elif request.method == 'PUT':
        result = find_client(id)
        if result:
            # aplicamos destructuracion para tener mejor entendimiento de las variables
            [usuario, posicion] = result
            data = request.get_json()
            data['id'] = id
            clients[posicion] = data
            return {
                'message': 'Cliente actualizado',
                'clients': clients
            }
        return {
            'message': 'No se encontro el cliente'
        }, 404
    elif request.method == 'DELETE':
        result = find_client(id)
        if result:
            # aplicamos destructuracion para tener mejor entendimiento de las variables
            [usuario, posicion] = result
            clients.pop(posicion)
            return {
                'message': 'Cliente eliminado',
                'clients': clients
            }
        return {
            'message': 'No se encontro el cliente'
        }, 404

# el port indicara el numero de puerto a usar
app.run(debug=True, port = 5000)
