# Generated by Django 4.2.5 on 2023-09-20 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0006_paciente_genero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='genero',
            field=models.CharField(default='masculino', max_length=12),
        ),
    ]