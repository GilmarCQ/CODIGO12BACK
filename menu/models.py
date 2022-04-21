from django.db import models
from cloudinary import models as modelsCloudinary

# Create your models here.


class Plato(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45, null=False)
    foto = modelsCloudinary.CloudinaryField(
        folder='plato'
    )
    disponible = models.BooleanField(default=True, null=False)
    precio = models.FloatField(null=False)

    class Meta:
        db_table = 'platos'

class Stock(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField(null=False)
    cantidad = models.IntegerField(null=False)
    precio_diario = models.FloatField(null=False)

    # relared_name  >   sirve para crear la relacion con otra tabla (en este caso se crea la relacion con platos)
    # on_delete     >   restriccion que toima distintas propiedades cuando se elimina el padre de la fk
    #   CASCADE     >   elimina el plato y todas la relaciones hiujo que tenga
    #   PROTECT     >   impedira que se elimina el padre si tiene relaciones hijo creadas
    #   SET_NULL    >   elimina la relacion padre, y colocara null en los fk dependientes
    #   DO_NOTHING  >   elimina la relacion padre y no hace nada mas
    #   RESTRICT    >   no permite la eliminacion y lanzara un error

    platoId = models.ForeignKey(to=Plato, related_name='stocks', on_delete=models.CASCADE)

    class Meta:
        db_table = 'stocks'

        # unique_together   >   crea un indice de dos o mas columnas en el cual no se podra repetir los nismos valores
        # de esas columnas
        # fecha         |   platoId
        # 2022-04-18    |   1       ERROR
        # 2022-04-18    |   1       ERROR
        # 2022-04-18    |   2       CORRECTO
        # 2022-04-19    |   1       CORRECTO
        unique_together = [['fecha', 'platoId']]
