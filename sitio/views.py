from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Salas
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

def agregar_sala (request):
    return render(request, 'agregar_sala.html') 

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