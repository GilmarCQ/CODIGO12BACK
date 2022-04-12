from django.db import models


# Create your models here.

class Etiqueta(models.Model):
    # https://docs.djangoproject.com/en/4.0/ref/models/fields/#field-types
    # https://docs.djangoproject.com/en/4.0/ref/models/fields/#field-options
    id = models.AutoField(primary_key=True, unique=True, null=False)
    nombre = models.CharField(max_length=80, unique=True, null=False)

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


class Tareas(models.Model):
    class CategoriaOpciones(models.TextChoices):
        TODO = 'TODO', 'TO_DO'
        IN_PROGRESS = 'IP', 'IN_PROGRESS'
        DONE = 'DONE', 'DONE'
        CANCELLED = 'CANCELLED', 'CANCELLED'

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45, null=False)
    categoria = models.CharField(max_length=45, choices=CategoriaOpciones.choices, default=CategoriaOpciones.TODO)

    # Forma 2 usando una lista de tuplas
    # categoria = models.CharField(max_length=45, choices=[
    #     ('TODO', 'TO_DO'),
    #     ('IP', 'IN_PROGRESS'),
    #     ('DONE', 'DONE'),
    #     ('CANCELLED', 'CANCELLED')
    # ], default='TODO')

    fechaCaducidad = models.DateTimeField(db_column='fecha_caducidad')
    importancia = models.IntegerField(null=False)

    descripcion = models.TextField(null=True)

    createdAt = models.DateTimeField(auto_now_add=True, db_column='created_at')
    updatedAt = models.DateTimeField(auto_now=True, db_column='updated_at')

    etiquetas = models.ManyToManyField(to=Etiqueta, related_name='tareas')

    foto = models.ImageField(
        upload_to='multimedia',
        null=True
    )

    class Meta:
        db_table = 'tareas'


#     Si la tabla tareas_etiquetas no fuese una tabla pivote, en ese caso se tendria que crear la tabla como una
#     tabla comun y corriente
# class TareasEqtiquetas(models.Model):
#     etiquetaFK = models.ForeignKey(to=Etiquetas)
#     tareaFK = models.ForeignKey(to=Tareas)
