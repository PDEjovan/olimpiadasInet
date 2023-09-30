from django.db import models

class Obra_Social(models.Model):
    nombre=models.CharField(max_length=30)

class Enfermeros(models.Model):
    DNI = models.CharField(max_length=8)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    direccion = models.TextField()
    email = models.EmailField()
    fecha_nacimiento=models.DateField()
    genero=models.CharField(max_length=12, default='masculino')
    telefono = models.CharField(max_length=12) 

    

# Create your models here.
class Paciente(models.Model):
    matricula=models.CharField(max_length=10)
    DNI = models.CharField(max_length=8)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    direccion = models.TextField()
    email = models.EmailField()
    obra_social=models.ForeignKey(Obra_Social, on_delete=models.CASCADE)
    fecha_nacimiento=models.DateField(null=True)

    genero=models.CharField(max_length=12, default='masculino')
    
    telefono = models.CharField(max_length=12)  # Puedes ajustar el patrón de validación según tu necesidad

    alergia = models.CharField(max_length=255, blank=True, null=True)
    
    enfermedad_cronica = models.CharField(max_length=255, blank=True, null=True)
    
    tratamiento_medico = models.CharField(max_length=255, blank=True, null=True)
    
    enfermedades_o_cirugias = models.TextField(blank=True, null=True)

    enfermero=models.ForeignKey(Enfermeros,on_delete=models.CASCADE)


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
    direccion = models.TextField()
    email = models.EmailField()
    telefono = models.CharField(max_length=12) 
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
    email=models.EmailField()
    contraseña=models.CharField(max_length=50 )
    tipo_user=models.BooleanField(default=False)

class Salas(models.Model):
    nombre=models.CharField(max_length=50)
    tipo_sala=models.CharField(max_length=50)