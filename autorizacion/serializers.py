from rest_framework import serializers
from .models import Usuario


class RegistroUsuarioSerializer(serializers.ModelSerializer):

    def save(self):
        nuevoUsuario = Usuario(**self.validated_data)
        nuevoUsuario.set_password(self.validated_data.get('password'))
        nuevoUsuario.save()
        return nuevoUsuario

    class Meta:
        model = Usuario
        # fields = '__all__'
        exclude = ['groups', 'user_permissions']
        extra_kwargs = {
            'password': {
                'write_only': True
            },
            'id': {
                'read_only': True
            }
        }


