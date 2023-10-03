# Generated by Django 4.2.5 on 2023-10-03 00:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0013_llamados_estado'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('Medico', 'Médico'), ('Enfermero', 'Enfermero'), ('Recepcionista', 'Recepcionista')], max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='sitio.user')),
            ],
        ),
    ]