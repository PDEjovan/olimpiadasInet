
import os
import django
from django.contrib.auth.models import Group
# Establece la variable de entorno DJANGO_SETTINGS_MODULE



def crear_grupos():

    # Crear un grupo llamado "Médicos"

    grupo_medicos, creado1 = Group.objects.get_or_create(name='Médicos')

    # Crear un grupo llamado "Enfermeros"
    grupo_enfermeros, creado2 = Group.objects.get_or_create(name='Enfermeros')

    # Crear un grupo llamado "Recepcionistas"
    grupo_recepcionistas, creado3 = Group.objects.get_or_create(name='Recepcionistas')


if __name__ == '__main__':
    crear_grupos()
