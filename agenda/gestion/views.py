from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.generics import (ListAPIView,
                                     ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView,
                                     CreateAPIView,
                                     DestroyAPIView)
from .serializers import (PruebaSerializer,
                          TareasSerializer,
                          EtiquetaSerializer,
                          TareaSerializer,
                          TareaPersonalizableSerializer,
                          ArchivoSerializer,
                          EliminarArchivoSerializer)
from .models import Tareas, Etiqueta
from rest_framework import status
from django.utils import timezone
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from os import remove
from django.conf import settings


# https://www.django-rest-framework.org/api-guide/requests/

@api_view(http_method_names=['GET', 'POST'])
def inicio(request: Request):
    print(request.method)
    # print(request)
    if request.method == 'GET':
        return Response(data={
            'message': 'Bienvenido a mi API de agenda'
        })
    elif request.method == 'POST':
        return Response(data={
            'message': 'Hiciste un POST'
        }, status=201)


class PruebaApiView(ListAPIView):
    # sirve para ayudarnos para cuando se llame a este request nos haga el trabajo de serializar la informacion,
    # es igual a un DTO
    serializer_class = PruebaSerializer
    # queryset, es el encargado de buscar en el controlador (para todos sus metodos)
    queryset = [{
        'nombre': 'Gilmar',
        'apellido': 'Campana Quispe',
        'correo': 'gacampanaq@gmail.com',
        'dni': '72690553',
        'estado_civil': 'soltero'
    }]

    def get(self, request: Request):
        # si se definen los metooos GET, POST, etc se omiten el serializador y el queryset

        informacion = self.queryset
        # se llama al serializador y se realizador el filtrado de la misma
        # la opcion many=True, permite trabajar con listas
        informacion_serializada = self.serializer_class(data=informacion, many=True)

        # se hace la validacion de que la informacion serializada es correcta, de no ser asi con la opcion
        # raise_exception lanzara un error
        informacion_serializada.is_valid(raise_exception=True)

        return Response(data={
            'message': 'Hola GET',
            'content': informacion_serializada.data
        })


class TareasApiView(ListCreateAPIView):
    queryset = Tareas.objects.all()  # SELECT * FROM tareas
    serializer_class = TareasSerializer

    def post(self, request: Request):
        serializador = self.serializer_class(data=request.data)
        if serializador.is_valid():
            # serializador.initial_data > data inicial sin validacion
            # serializador.validated_data > data ya validada (solo se puede llamar despues del metodo is_valid())
            fechaCaducidad = serializador.validated_data.get('fechaCaducidad')
            importancia = serializador.validated_data.get('importancia')
            if importancia < 0 or importancia > 10:
                return Response(data={
                    'message': 'La importancia debe estar entre 1-10'
                }, status=status.HTTP_400_BAD_REQUEST)

            if timezone.now() > fechaCaducidad:
                return Response(data={
                    'message': 'La fecha no puede ser menor que la fecha actual'
                }, status=status.HTTP_400_BAD_REQUEST)
            # el metodo save() se podra llamar siempre en cuando sea un ModelSerializer, la cual actualizara la bd
            serializador.save()
            return Response(data=serializador.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data={
                'message': 'La data no es válida',
                'content': serializador.errors},
                status=status.HTTP_400_BAD_REQUEST)


class EtiquetasApiView(ListCreateAPIView):
    queryset = Etiqueta.objects.all()
    serializer_class = EtiquetaSerializer


class TareaApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = TareaSerializer
    queryset = Tareas.objects.all()


class ArchivosApiView(CreateAPIView):
    serializer_class = ArchivoSerializer

    def post(self, request: Request):
        # FILES, para ingresart a los archivos provenientes del form-data se usa el FILES
        data = self.serializer_class(data=request.FILES)
        carpetaDestino = request.query_params.get('modelo')

        if data.is_valid():
            print(data.validated_data.get('archivo'))
            archivo: InMemoryUploadedFile = data.validated_data.get('archivo')
            print(archivo.size)
            if archivo.size > (5120 * 1024):
                return Response(data={
                    'message': 'Archivo muy grande, no puede ser mas de 5Mb',
                    'content': data.errors
                }, status=status.HTTP_400_BAD_REQUEST)

            resultado = default_storage.save(
                (carpetaDestino + '/' if carpetaDestino is not None else '') + archivo.name, ContentFile(archivo.read())
            )
            print(resultado)
            return Response(data={
                'message': 'Archivo guardado exitosamente.',
                'content': {
                    'ubicacion': resultado
                }
            }, status=status.HTTP_201_CREATED)
        else:
            return Response(data={
                'message': 'Error al intentar la imagen',
                'content': data.errors
            }, status=status.HTTP_400_BAD_REQUEST)

class EliminarArchivoApiView(DestroyAPIView):
    # por defecto el DestroyAPIView solicita un pk para para eliminar un registro determinado , en este caso se
    # hara una personalizacion poara que realize la eliminacion
    serializer_class = EliminarArchivoSerializer
    def delete(self, request: Request):
        data = self.serializer_class(data = request.data)
        try:
            if data.is_valid():
                ubicacion = data.validated_data.get('archivo')
                # eliminara el archivo ubicado en esa direccion
                remove(settings.MEDIA_ROOT / ubicacion)
                return Response(data = {
                    'message': 'Archivo eliminado exitosamente'
                })
            else:
                return Response(data = {
                    'message': 'Error al eliminar el archivo',
                    'content': data.errors
                })
        except Exception as e:
            return Response(data = {
                'message': 'No se encontro el archivo a eliminar',
                'content': e.args
            }, status=status.HTTP_404_NOT_FOUND)
