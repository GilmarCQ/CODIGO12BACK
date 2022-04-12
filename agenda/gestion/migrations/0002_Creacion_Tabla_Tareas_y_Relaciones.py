# Generated by Django 4.0.3 on 2022-04-06 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0001_Creacion_Tabla_Etiquetas'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tareas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
                ('categoria', models.CharField(choices=[('TODO', 'TO_DO'), ('IP', 'IN_PROGRESS'), ('DONE', 'DONE'), ('CANCELLED', 'CANCELLED')], default='TODO', max_length=45)),
                ('fechaCaducidad', models.DateTimeField(db_column='fecha_caducidad')),
                ('importancia', models.IntegerField()),
                ('createdAt', models.DateTimeField(auto_now_add=True, db_column='created_at')),
                ('updatedAt', models.DateTimeField(auto_now=True, db_column='updated_at')),
                ('etiquetas', models.ManyToManyField(related_name='tareas', to='gestion.etiqueta')),
            ],
            options={
                'db_table': 'tareas',
            },
        ),
    ]
