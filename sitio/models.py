from django.db import models

class Obra_Social(models.Model):
    nombre=models.CharField(max_length=30)

# Create your models here.
class Paciente (models.Model):
    DNI=models.CharField(max_length=8)
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=100)
    direccion=models.TextField()
    telefono=models.CharField(max_length=15)
    email=models.EmailField()
    obra_social=models.ForeignKey(Obra_Social, on_delete=models.CASCADE)
    
class Zonas(models.Model):
    nombre=models.CharField(max_length=50)
    tipo=models.CharField(max_length=50)

class Especialidad(models.Model):
    nombre=models.CharField(max_length=100)

class Medico(models.Model):
    DNI=models.CharField(max_length=8)
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=100)
    matricula=models.CharField(max_length=10)
    estado=models.BooleanField(default=False)
    especialidad=models.ForeignKey(Especialidad,on_delete=models.CASCADE)

class Llamados(models.Model):
    tipo_llamado=models.BooleanField(default=False)
    fecha_hora=models.DateTimeField()
    id_paciente=models.ForeignKey(Paciente,on_delete=models.CASCADE)
    id_zona=models.ForeignKey(Zonas,on_delete=models.CASCADE)
    id_medico=models.ForeignKey(Medico,on_delete=models.CASCADE)

class User(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=100)
    telefono=models.CharField(max_length=15)
    direccion=models.TextField()
    email=models.EmailField()
    contraseña=models.CharField(max_length=50 )
    tipo_user=models.BooleanField(default=False)