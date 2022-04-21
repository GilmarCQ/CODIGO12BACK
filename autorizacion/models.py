from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
# AbstractBaseUser permire modificar todo el modelo auth user desde 0, quita o agrega columnas sobre las que se tiene
from .authManager import UserManager


class Usuario(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    correo = models.EmailField(null=False, unique=True)
    password = models.TextField(null=False)
    nombre = models.CharField(max_length=45, null=False)
    rol = models.CharField(choices=(
        ['ADMINISTRADOR', 'ADMINISTRADOR'],
        ['MOZO', 'MOZO']), max_length=40)

    # para el panel administrativo se debe colocar el siguiente campo, is_staff
    # indica si el usuario creado podra ingresar al panel administrativo
    is_staff = models.BooleanField(default=False)
    # permite que el usuario se loguee, si es false no permitira realizar ninguna accion
    is_active = models.BooleanField(default=True)

    createdAt = models.DateTimeField(auto_now_add=True, db_column='created_at')

    # comportamiento que tendra el modelo cuando se realize el comando cretesuperuser
    objects = UserManager()

    #   este sera solicitado en el login del admin de django
    USERNAME_FIELD = 'correo'

    # atributos que se solcitaran por consola al momento de crear el super usuario, no se debe poner los campos
    # especificados en el USERNAME_FIELD y el password
    REQUIRED_FIELDS = ['nombre', 'rol']

    class Meta:
        db_table = 'usuarios'