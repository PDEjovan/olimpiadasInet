# Generated by Django 4.2.5 on 2023-09-17 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Salas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('tipo_sala', models.CharField(max_length=50)),
            ],
        ),
    ]
