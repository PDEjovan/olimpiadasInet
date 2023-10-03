from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

class Enfermeros(models.Model):
    DNI = models.CharField(max_length=8)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    direccion = models.TextField()
    email = models.EmailField()
    fecha_nacimiento=models.DateField()
    genero=models.CharField(max_length=12, default='masculino')
    telefono = models.CharField(max_length=12)
    lunesMI = models.TimeField(null=True)
    lunesMF = models.TimeField(null=True)
    lunesTI = models.TimeField(null=True)
    lunesTF = models.TimeField(null=True)
    martesMI = models.TimeField(null=True)
    martesMF = models.TimeField(null=True)
    martesTI = models.TimeField(null=True)
    martesTF = models.TimeField(null=True)
    miercolesMI = models.TimeField(null=True)
    miercolesMF = models.TimeField(null=True)
    miercolesTI = models.TimeField(null=True)
    miercolesTF = models.TimeField(null=True)
    juevesMI = models.TimeField(null=True)
    juevesMF = models.TimeField(null=True)
    juevesTI = models.TimeField(null=True)
    juevesTF = models.TimeField(null=True)
    viernesMI = models.TimeField(null=True)
    viernesMF = models.TimeField(null=True)
    viernesTI = models.TimeField(null=True)
    viernesTF = models.TimeField(null=True)
    sabadoMI = models.TimeField(null=True)
    sabadoMF = models.TimeField(null=True)
    sabadoTI = models.TimeField(null=True)
    sabadoTF = models.TimeField(null=True)
    domingoMI = models.TimeField(null=True)
    domingoMF = models.TimeField(null=True)
    domingoTI = models.TimeField(null=True)
    domingoTF = models.TimeField(null=True)


class Salas(models.Model):
    nombre=models.CharField(max_length=50)
    tipo_sala=models.CharField(max_length=50)
# Create your models here.
class Paciente(models.Model):
    DNI = models.CharField(max_length=8)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    direccion = models.TextField()
    email = models.EmailField()
    obra_social=models.CharField(max_length=30)
    fecha_nacimiento=models.DateField(null=True)
    genero=models.CharField(max_length=12, default='masculino')
    telefono = models.CharField(max_length=12)  # Puedes ajustar el patrón de validación según tu necesidad
    alergia = models.CharField(max_length=255, blank=True, default='No',null=True)
    enfermedad_cronica = models.CharField(max_length=255, blank=True, default='No',null=True)
    tratamiento_medico = models.CharField(max_length=255, blank=True, default='No',null=True)
    enfermedades_o_cirugias = models.TextField(max_length=255, blank=True, default='No',null=True)
    enfermero=models.ForeignKey(Enfermeros,on_delete=models.CASCADE)
    internado=models.CharField(max_length=2, default='No')
    sala=models.ForeignKey(Salas,on_delete=models.CASCADE)


class Medico(models.Model):
    DNI=models.CharField(max_length=8)
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=100)
    matricula=models.CharField(max_length=10)
    direccion = models.TextField()
    email = models.EmailField()
    telefono = models.CharField(max_length=12) 
    estado=models.BooleanField(default=False)
    especialidad=models.CharField(max_length=100)
    genero=models.CharField(max_length=12, default='Masculino')
    fecha_nacimiento=models.DateField()
    lunesMI = models.TimeField(null=True)
    lunesMF = models.TimeField(null=True)
    lunesTI = models.TimeField(null=True)
    lunesTF = models.TimeField(null=True)
    martesMI = models.TimeField(null=True)
    martesMF = models.TimeField(null=True)
    martesTI = models.TimeField(null=True)
    martesTF = models.TimeField(null=True)
    miercolesMI = models.TimeField(null=True)
    miercolesMF = models.TimeField(null=True)
    miercolesTI = models.TimeField(null=True)
    miercolesTF = models.TimeField(null=True)
    juevesMI = models.TimeField(null=True)
    juevesMF = models.TimeField(null=True)
    juevesTI = models.TimeField(null=True)
    juevesTF = models.TimeField(null=True)
    viernesMI = models.TimeField(null=True)
    viernesMF = models.TimeField(null=True)
    viernesTI = models.TimeField(null=True)
    viernesTF = models.TimeField(null=True)
    sabadoMI = models.TimeField(null=True)
    sabadoMF = models.TimeField(null=True)
    sabadoTI = models.TimeField(null=True)
    sabadoTF = models.TimeField(null=True)
    domingoMI = models.TimeField(null=True)
    domingoMF = models.TimeField(null=True)
    domingoTI = models.TimeField(null=True)
    domingoTF = models.TimeField(null=True)


class Llamados(models.Model):
    tipo_llamado=models.CharField(max_length=20)
    fecha_hora=models.DateTimeField(default=timezone.now)
    diagnostico=models.CharField(max_length=50,default='nada')
    id_paciente=models.ForeignKey(Paciente,on_delete=models.CASCADE)
    id_zona=models.ForeignKey(Salas,on_delete=models.CASCADE)
    id_medico=models.ForeignKey(Medico,on_delete=models.CASCADE)
    estado=models.BooleanField(default=False)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role_choices = [
        ('Medico', 'Médico'),
        ('Enfermero', 'Enfermero'),
        ('Recepcionista', 'Recepcionista'),
    ]
    role = models.CharField(max_length=20, choices=role_choices)

    # Agrega otros campos personalizados según sea necesario

    def __str__(self):
        return self.user.username
    
