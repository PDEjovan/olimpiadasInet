# Generated by Django 4.2.5 on 2023-10-01 23:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0003_rename_enfermedades_o_cirugias_paciente_cirugias_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paciente',
            old_name='cirugias',
            new_name='enfermedades_o_cirugias',
        ),
        migrations.RemoveField(
            model_name='paciente',
            name='Salas',
        ),
    ]
