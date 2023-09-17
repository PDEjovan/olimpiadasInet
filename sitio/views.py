from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def index (request):
    return render (request, 'index.html')

def login (request):
    
    return render(request, 'login.html') 

def dashboard (request):
    return render(request, 'dashboard.html') 

def areas (request):
    return render(request, 'areas.html') 

def calls (request):
    return render(request, 'calls.html') 

def pacientes (request):
    return render(request, 'pacientes.html') 

def agregar_sala (request):
    return render(request, 'agregar_sala.html') 

def editar_sala (request):
    return render(request, 'editar_sala.html') 

def agregar_paciente (request):
    return render(request, 'agregar_pacientes.html')