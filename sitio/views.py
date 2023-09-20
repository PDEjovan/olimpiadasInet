from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Salas,Paciente,Obra_Social
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
    pacientess = Paciente.objects.all()
    return render(request, 'pacientes.html',{'pacientes':pacientess}) 

def editar_paciente (request,paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)
    if request.method == 'POST':
        # Obtén los datos del formulario
        dni = request.POST.get('DNI')
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        direccion = request.POST.get('direccion')
        email = request.POST.get('email')
        obra_so = request.POST.get('obra_social')
        genero = request.POST.get('example-radio')
        telefono = request.POST.get('telf')
        alergia = request.POST.get('alergia')
        enfermedad_cronica = request.POST.get('enf_cro')
        tratamiento_medico = request.POST.get('tratamiento')
        enfermedades_o_cirugias = request.POST.get('enf_cir')
        año_fecha_nac= request.POST.get('año')
        dia_fecha_nac= request.POST.get('dia')
        mes_fecha_nac= request.POST.get('mes')
        fecha = año_fecha_nac + "-" + mes_fecha_nac + "-" + dia_fecha_nac
        obra_social = Obra_Social.objects.get(nombre=obra_so)
        # Actualiza los datos de la paciente
        paciente.DNI = dni
        paciente.nombre = nombre
        paciente.apellido = apellido
        paciente.direccion = direccion
        paciente.email = email
        paciente.obra_social = obra_social
        paciente.genero = genero
        paciente.telefono = telefono
        paciente.alergia = alergia
        paciente.enfermedad_cronica = enfermedad_cronica
        paciente.tratamiento_medico = tratamiento_medico
        paciente.enfermedades_o_cirugias = enfermedades_o_cirugias
        paciente.fecha_nacimiento = fecha
        paciente.save()

        return redirect('pacientes')  # Reemplaza 'lista_salas' con la URL correcta

    return render(request, 'editar_paciente.html',{'paciente': paciente}) 

def agregar_paciente (request):
    if request.method == 'POST':
        dni = request.POST.get('DNI')
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        direccion = request.POST.get('direccion')
        email = request.POST.get('email')
        obra_so = request.POST.get('obra_social')
        genero = request.POST.get('example-radio')
        telefono = request.POST.get('telf')
        alergia = request.POST.get('alergia')
        enfermedad_cronica = request.POST.get('enf_cro')
        tratamiento_medico = request.POST.get('tratamiento')
        enfermedades_o_cirugias = request.POST.get('enf_cir')
        año_fecha_nac= request.POST.get('año')
        dia_fecha_nac= request.POST.get('dia')
        mes_fecha_nac= request.POST.get('mes')

        fecha = año_fecha_nac + "-" + mes_fecha_nac + "-" + dia_fecha_nac
        obra_social = Obra_Social.objects.get(nombre=obra_so)
        email = request.POST.get('email')
        Paciente.objects.create(DNI=dni, nombre=nombre,apellido=apellido,direccion=direccion,email=email,obra_social=obra_social,fecha_nacimiento=fecha,genero=genero,telefono=telefono,alergia=alergia,enfermedad_cronica=enfermedad_cronica,tratamiento_medico=tratamiento_medico,enfermedades_o_cirugias=enfermedades_o_cirugias)

        return redirect('pacientes')  # Reemplaza 'lista_salas' con la URL correcta

    return render(request, 'agregar_pacientes.html')

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