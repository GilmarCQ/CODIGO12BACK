# from django.test import TestCase

from rest_framework.test import APITestCase


class EtiquetasTestCase(APITestCase):
    def test_crear_etiqueta_success(self):
        # se realiza la peticion al backend con data de prueba en el body
        request = self.client.post('/gestion/etiquetas', data={
            'nombre': 'FrontEnd'
        })
        # comparacion donde se valida que el status del request sea 201
        self.assertEqual(request.status_code, 201)

        # assertEqual > afirmamos que el primer parametro sera igual al segundo
        # self.assertEqual(1, 1)

    def test_listar_etiquetas_success(self):
        request = self.client.get('/gestion/etiquetas')
        print(request.data)
        self.assertEqual(1, 1)
