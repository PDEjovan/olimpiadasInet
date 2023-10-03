# Generated by Django 4.2.5 on 2023-10-03 03:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Enfermeros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DNI', models.CharField(max_length=8)),
                ('nombre', models.CharField(max_length=255)),
                ('apellido', models.CharField(max_length=255)),
                ('direccion', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('fecha_nacimiento', models.DateField()),
                ('genero', models.CharField(default='masculino', max_length=12)),
                ('telefono', models.CharField(max_length=12)),
                ('lunesMI', models.TimeField(null=True)),
                ('lunesMF', models.TimeField(null=True)),
                ('lunesTI', models.TimeField(null=True)),
                ('lunesTF', models.TimeField(null=True)),
                ('martesMI', models.TimeField(null=True)),
                ('martesMF', models.TimeField(null=True)),
                ('martesTI', models.TimeField(null=True)),
                ('martesTF', models.TimeField(null=True)),
                ('miercolesMI', models.TimeField(null=True)),
                ('miercolesMF', models.TimeField(null=True)),
                ('miercolesTI', models.TimeField(null=True)),
                ('miercolesTF', models.TimeField(null=True)),
                ('juevesMI', models.TimeField(null=True)),
                ('juevesMF', models.TimeField(null=True)),
                ('juevesTI', models.TimeField(null=True)),
                ('juevesTF', models.TimeField(null=True)),
                ('viernesMI', models.TimeField(null=True)),
                ('viernesMF', models.TimeField(null=True)),
                ('viernesTI', models.TimeField(null=True)),
                ('viernesTF', models.TimeField(null=True)),
                ('sabadoMI', models.TimeField(null=True)),
                ('sabadoMF', models.TimeField(null=True)),
                ('sabadoTI', models.TimeField(null=True)),
                ('sabadoTF', models.TimeField(null=True)),
                ('domingoMI', models.TimeField(null=True)),
                ('domingoMF', models.TimeField(null=True)),
                ('domingoTI', models.TimeField(null=True)),
                ('domingoTF', models.TimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DNI', models.CharField(max_length=8)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=100)),
                ('matricula', models.CharField(max_length=10)),
                ('direccion', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=12)),
                ('estado', models.BooleanField(default=False)),
                ('especialidad', models.CharField(max_length=100)),
                ('genero', models.CharField(default='Masculino', max_length=12)),
                ('fecha_nacimiento', models.DateField()),
                ('lunesMI', models.TimeField(null=True)),
                ('lunesMF', models.TimeField(null=True)),
                ('lunesTI', models.TimeField(null=True)),
                ('lunesTF', models.TimeField(null=True)),
                ('martesMI', models.TimeField(null=True)),
                ('martesMF', models.TimeField(null=True)),
                ('martesTI', models.TimeField(null=True)),
                ('martesTF', models.TimeField(null=True)),
                ('miercolesMI', models.TimeField(null=True)),
                ('miercolesMF', models.TimeField(null=True)),
                ('miercolesTI', models.TimeField(null=True)),
                ('miercolesTF', models.TimeField(null=True)),
                ('juevesMI', models.TimeField(null=True)),
                ('juevesMF', models.TimeField(null=True)),
                ('juevesTI', models.TimeField(null=True)),
                ('juevesTF', models.TimeField(null=True)),
                ('viernesMI', models.TimeField(null=True)),
                ('viernesMF', models.TimeField(null=True)),
                ('viernesTI', models.TimeField(null=True)),
                ('viernesTF', models.TimeField(null=True)),
                ('sabadoMI', models.TimeField(null=True)),
                ('sabadoMF', models.TimeField(null=True)),
                ('sabadoTI', models.TimeField(null=True)),
                ('sabadoTF', models.TimeField(null=True)),
                ('domingoMI', models.TimeField(null=True)),
                ('domingoMF', models.TimeField(null=True)),
                ('domingoTI', models.TimeField(null=True)),
                ('domingoTF', models.TimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Salas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('tipo_sala', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('Medico', 'Médico'), ('Enfermero', 'Enfermero'), ('Recepcionista', 'Recepcionista')], max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DNI', models.CharField(max_length=8)),
                ('nombre', models.CharField(max_length=255)),
                ('apellido', models.CharField(max_length=255)),
                ('direccion', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('obra_social', models.CharField(max_length=30)),
                ('fecha_nacimiento', models.DateField(null=True)),
                ('genero', models.CharField(default='masculino', max_length=12)),
                ('telefono', models.CharField(max_length=12)),
                ('alergia', models.CharField(blank=True, default='No', max_length=255, null=True)),
                ('enfermedad_cronica', models.CharField(blank=True, default='No', max_length=255, null=True)),
                ('tratamiento_medico', models.CharField(blank=True, default='No', max_length=255, null=True)),
                ('enfermedades_o_cirugias', models.TextField(blank=True, default='No', max_length=255, null=True)),
                ('internado', models.CharField(default='No', max_length=2)),
                ('enfermero', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sitio.enfermeros')),
                ('sala', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sitio.salas')),
            ],
        ),
        migrations.CreateModel(
            name='Llamados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_llamado', models.CharField(max_length=20)),
                ('fecha_hora', models.DateTimeField(default=django.utils.timezone.now)),
                ('diagnostico', models.CharField(default='nada', max_length=50)),
                ('estado', models.BooleanField(default=False)),
                ('id_medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sitio.medico')),
                ('id_paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sitio.paciente')),
                ('id_zona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sitio.salas')),
            ],
        ),
    ]
