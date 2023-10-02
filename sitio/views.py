from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Salas,User,Obra_Social,Enfermeros,Paciente,Especialidad,Medico,Llamados
# Create your views here.
@login_required
def index (request):
    return render (request, 'index.html')

def login (request):
    
    return render(request, 'login.html') 

def dashboard (request):
    return render(request, 'dashboard.html') 

def areas (request):
    salas = Salas.objects.all()
    return render(request, 'areas.html',{'salas': salas}) 

def calls (request):
    return render(request, 'calls.html') 

def pacientes (request):
    return render(request, 'pacientes.html') 

def agregar_paciente (request):
    salas = Salas.objects.all()
    return render(request, 'agregar_pacientes.html', {'salas': salas}) 
     


def perfil_paciente (request):
    return render(request, 'perfil_paciente.html') 

def tabla_pacientes (request):
    return render(request, 'tabla_pacientes.html') 


def editar_paciente (request):
    salas = Salas.objects.all()
    return render(request, 'editar_paciente.html', {'salas': salas}) 

def agregar_sala (request):
    return render(request, 'agregar_sala.html') 

def medicos (request):
    return render(request, 'medicos.html')

def enfermeros (request):
    return render(request, 'enfermeros.html') 

def perfil_enfermero (request):
    return render(request, 'perfil_enfermero.html')

def perfil_medico (request):
    return render(request, 'perfil_medico.html')

def agregar_enfermero (request):
    return render(request, 'agregar_enfermero.html') 

def agregar_medico (request):
    return render(request, 'agregar_medico.html') 

def editar_enfermero (request):
    return render(request, 'editar_enfermero.html') 

def editar_medico (request):
    return render(request, 'editar_medico.html')

def users (request):
    users = User.objects.all()
    return render(request, 'users.html',{'users': users})

def editar_users (request, user_id):
    users = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        # Obtén los datos del formulario
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        telefono = request.POST.get('telefono')
        email = request.POST.get('email')
        contraseña = request.POST.get('password')

        # Actualiza los datos del usuario
        users.nombre = nombre
        users.apellido = apellido
        users.telefono = telefono
        users.email = email
        users.contraseña = contraseña
        users.save()

        return redirect('users')

    return render(request, 'editar_users.html', {'users':users})  

def agregar_users (request):
    return render(request, 'agregar_users.html')  

def historial_clinico (request):
    return render(request, 'historial_clinico.html')  

def historial_llamadas (request):
    return render(request, 'historial_llamadas.html')  

def atender_calls (request):
    return render(request, 'atender_calls.html')  


def editar_sala (request, sala_id):
    sala = get_object_or_404(Salas, id=sala_id)
    if request.method == 'POST':
        # Obtén los datos del formulario
        nombre = request.POST.get('nombre')
        tipo = request.POST.get('select_salas')

        # Actualiza los datos de la sala
        sala.nombre = nombre
        sala.tipo_sala = tipo
        sala.save()

        return redirect('areas')  # Reemplaza 'lista_salas' con la URL correcta

    return render(request, 'editar_sala.html', {'sala': sala})

def procesar_formulario(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        tipo = request.POST.get('select_salas')

        Salas.objects.create(nombre=nombre, tipo_sala=tipo)

        return redirect('areas')  # Reemplaza 'lista_salas' con la URL correcta

    return render(request, 'agregar_sala.html')

def procesar_formulario_users(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        telefono = request.POST.get('telefono')
        email = request.POST.get('email')
        contraseña = request.POST.get('password')

        User.objects.create(nombre=nombre, apellido=apellido, telefono=telefono, email=email, contraseña=contraseña, )

        return redirect('users') 

    return render(request, 'agregar_users.html')

def eliminar_objeto(request,modelo ,objeto_id):
    if modelo == "User":

        objeto_a_eliminar = get_object_or_404(User, id=objeto_id)
        objeto_a_eliminar.delete()

        return redirect('users')  # Redirige a donde desees después de eliminar el objeto
    
    elif modelo == "Salas":

        objeto_a_eliminar = get_object_or_404(Salas, id=objeto_id)
        objeto_a_eliminar.delete()

        return redirect('areas')  # Redirige a donde desees después de eliminar el objeto
    
    elif modelo == "Obra_Social":

        objeto_a_eliminar = get_object_or_404(Obra_Social, id=objeto_id)
        objeto_a_eliminar.delete()

        return redirect('users')  # Redirige a donde desees después de eliminar el objeto
    
    elif modelo == "Enfermeros":

        objeto_a_eliminar = get_object_or_404(Enfermeros, id=objeto_id)
        objeto_a_eliminar.delete()

        return redirect('enfermeros')  # Redirige a donde desees después de eliminar el objeto
    
    elif modelo == "Paciente":

        objeto_a_eliminar = get_object_or_404(Paciente, id=objeto_id)
        objeto_a_eliminar.delete()

        return redirect('paciente')  # Redirige a donde desees después de eliminar el objeto
    
    elif modelo == "Zonas":

        objeto_a_eliminar = get_object_or_404(Zonas, id=objeto_id)
        objeto_a_eliminar.delete()

        return redirect('users')  # Redirige a donde desees después de eliminar el objeto

    elif modelo == "Medico":

        objeto_a_eliminar = get_object_or_404(Medico, id=objeto_id)
        objeto_a_eliminar.delete()

        return redirect('medicos')  # Redirige a donde desees después de eliminar el objeto

    elif modelo == "Llamados":

        objeto_a_eliminar = get_object_or_404(Llamados, id=objeto_id)
        objeto_a_eliminar.delete()

        return redirect('calls')  # Redirige a donde desees después de eliminar el objeto


    