# Generated by Django 4.2.5 on 2023-09-13 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0010_delete_customuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='nombre',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]