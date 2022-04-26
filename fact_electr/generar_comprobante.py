from .models import Comprobante, Pedido
import requests
from os import environ

# from django.db import connection


def generar_comprobante(tipo_de_comprobante: int, tipo_documento: str, numero_documento: str, pedido_id: int):

    pedido = Pedido.objects.filter(id=pedido_id).first()
    if pedido is None:
        raise Exception('Pedido no existe')

    if pedido.total > 700 and tipo_documento is None:
        raise Exception(
            'El pedido al tener un monto mayor a 700 soles debe tener un cliente registrado.'
        )
    operacion = 'generar comprobante'
    tipo = ''
    sunat_transaction = 1
    if tipo_de_comprobante == 1:
        serie = 'FFF1'
        tipo = 'FACTURA'
    elif tipo_de_comprobante == 2:
        serie = 'BBB1'
        tipo = 'BOLETA'
    elif tipo_de_comprobante == 3 or tipo_de_comprobante == 4:
        serie = '0001'
        tipo = 'NOTA'

    #   el numero se sacara del ultimo comprobante en la base de datos

    # with connection.cursor() as cursor:
    #     cursor.execute('SELECT * FROM vista_prueba')
    #     print(cursor.fetchall())

    ultimoComprobante = Comprobante.objects.values_list('numero', 'serie').filter(tipo=tipo).order_by('-numero').first()

    if ultimoComprobante is None:
        numero = 1
    else:
        numero = int(ultimoComprobante[0]) + 1

    if tipo_documento is None:
        cliente_tipo_documento = '-'
        cliente_numero_documento = None
    else:
        cliente_tipo_documento = tipo_documento
        cliente_numero_documento = numero_documento
        cliente_denominacion = ''
        if tipo_documento == 'RUC':
            respuesta_apiperu = requests.get('https://apiperu.dev/api/ruc/'+numero_documento,
                         headers={'Authorization': 'Bearer '+environ.get('APIPERU_TOKEN')})

            if respuesta_apiperu.json().get('success') is False:
                raise Exception('Datos del Cliente no válidos.')
            else:
                cliente_denominacion = respuesta_apiperu.json().get('data').get('nombre_o_razon_social')
        elif tipo_documento == 'DNI':
            respuesta_apiperu = requests.get('https://apiperu.dev/api/dni/'+numero_documento,
                         headers={'Authorization': 'Bearer '+environ.get('APIPERU_TOKEN')})

            if respuesta_apiperu.json().get('success') is False:
                raise Exception('Datos del Cliente no válidos.')
            else:
                cliente_denominacion = respuesta_apiperu.json().get('data').get('nombre_completo')

