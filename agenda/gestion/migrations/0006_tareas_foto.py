# Generated by Django 4.0.3 on 2022-04-09 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0005_Tabla_Etiqueta_Tamaño_nombre'),
    ]

    operations = [
        migrations.AddField(
            model_name='tareas',
            name='foto',
            field=models.ImageField(null=True, upload_to='multimedia'),
        ),
    ]