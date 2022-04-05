from django.db import models


# Create your models here.

class Etiqueta(models.Model):
    # https://docs.djangoproject.com/en/4.0/ref/models/fields/#field-types
    # https://docs.djangoproject.com/en/4.0/ref/models/fields/#field-options
    id = models.AutoField(primary_key=True, unique=True, null=False)
    nombre = models.CharField(max_length=8, unique=True, null=False)

    # columnas de auditoria
    # son columnas que ayudan a dar seguimiento a los registros
    # createdAt >   es la fecha en la cual se crea el registro
    createdAt = models.DateTimeField(auto_now_add=True, db_column='created_at')
    # updatedAt >   es la fecha en la cual se modifica un registro
    updatedAt = models.DateTimeField(auto_now=True, db_column='deleted_at')


    # configuraciones propias de la tabla
    # https://docs.djangoproject.com/en/4.0/ref/models/options/
    class Meta:
        # cambia el nombre de la tabla en la bd
        db_table = 'etiquetas'
        # modifica el ordednamiento natural (default id) e imponiendo el propio que sea DESC nombre, esta utilidad
        # solo funcionara en el get
        ordering = ['-nombre']
