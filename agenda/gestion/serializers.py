from rest_framework import serializers
from .models import Tareas, Etiqueta


class PruebaSerializer(serializers.Serializer):
    nombre = serializers.CharField(max_length=40, trim_whitespace=True)
    apellido = serializers.CharField()
    correo = serializers.EmailField()
    dni = serializers.RegexField(max_length=8, min_length=8, regex='[0-9]')


class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tareas
        fields = '__all__'
        depth = 1


class TareasSerializer(serializers.ModelSerializer):
    # se hace la modificacion del modeloy se setea la nueva configuracion del serializador
    # RESTRICCIONES: Si en el modelo es un IntegerField en el serializador no se podra cambiar a CharField al
    # guardar la data
    foto = serializers.CharField(max_length=100)

    class Meta:
        model = Tareas
        fields = '__all__'
        #   exclude = ['importancia'] # indica que columnas no se quiere utilizar
        #   no se puede utilizar los dos a la vez, uno indica que campos se usaran (fields) y el otro que campos se
        #   omitiran (exclude)
        extra_kwargs = {
            'etiquetas': {
                'write_only': True
            }
        }

        # depth = 1
        # Sirve para que en el caso que querramos devolver la informacion de una relacion entre este modelo
        # podemos indicar hasta que grado de profundidad queremos que nos devuelva la informacion,
        # la profundida maxima es de 10

        # depth, la profundidad solo se puede realizar donde el modelo que estamos utilizando ha sido declarado


class EtiquetaSerializer(serializers.ModelSerializer):
    # read_only, indica que el serializador aplicara el filtro solo para metodos de consulta
    tareas = TareasSerializer(many=True, read_only=True)  # , source='tareas'

    class Meta:
        model = Etiqueta
        fields = '__all__'
        depth = 1

        extra_kwargs = {
            # 'nombre': {'write_only': True},
            'id': {'read_only': True}
        }
        read_only_fields = ['createdAt']


# se usara para valdiar que el campo nombre no se pueda editar on el attributo read_only
class TareaPersonalizableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tareas
        fields = '__all__'
        extra_kwargs = {
            'nombre': {
                'read_only': True
            }
        }


class ArchivoSerializer(serializers.Serializer):
    archivo = serializers.ImageField(max_length=100, use_url=True)

class EliminarArchivoSerializer(serializers.Serializer):
    archivo = serializers.CharField(max_length=100)

