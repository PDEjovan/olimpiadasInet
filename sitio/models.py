from django.db import models

class Obra_Social(models.Model):
    nombre=models.CharField(max_length=30)

# Create your models here.
class Paciente(models.Model):
    DNI = models.CharField(max_length=8)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    direccion = models.TextField()
    email = models.EmailField()
    obra_social=models.ForeignKey(Obra_Social, on_delete=models.CASCADE)
    
    
    telefono = models.CharField(max_length=12)  # Puedes ajustar el patrón de validación según tu necesidad

    tiene_alergia = models.BooleanField(default=False)
    alergia = models.CharField(max_length=255, blank=True, null=True)
    
    tiene_enfermedad_cronica = models.BooleanField(default=False)
    enfermedad_cronica = models.CharField(max_length=255, blank=True, null=True)
    
    bajo_tratamiento_medico = models.BooleanField(default=False)
    tratamiento_medico = models.CharField(max_length=255, blank=True, null=True)
    
    ha_tenido_enfermedades_o_cirugias = models.BooleanField(default=False)
    enfermedades_o_cirugias = models.TextField(blank=True, null=True)
    
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

class Salas(models.Model):
    nombre=models.CharField(max_length=50)
    tipo_sala=models.CharField(max_length=50)