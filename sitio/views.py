from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Salas,User,Enfermeros,Paciente,Medico,Llamados
from .forms import RegistrationForm
from django.contrib.auth.models import User, Group
from django.contrib import messages
from .models import *
from django.contrib.auth import login
# Create your views here.

def is_medico_recepcionista_o_enfermero(user):
    # Verifica si el usuario es médico, recepcionista o enfermero
    return (
        user.groups.filter(name='Médico').exists() or
        user.groups.filter(name='Recepcionista').exists() or
        user.groups.filter(name='Enfermero').exists() or
        user.groups.filter(name='ADMIN').exists()
    )

def is_medico_admin_o_enfermero(user):
    # Verifica si el usuario es médico, recepcionista o enfermero
    return (
        user.groups.filter(name='Médico').exists() or
        user.groups.filter(name='Enfermero').exists() or
        user.groups.filter(name='ADMIN').exists()
    )

def is_medico_admin(user):
    # Verifica si el usuario es médico, recepcionista o enfermero
    return (
        user.groups.filter(name='Médico').exists() or
        user.groups.filter(name='ADMIN').exists()
    )

def is_admin(user):
    # Verifica si el usuario es médico, recepcionista o enfermero
    return (
        user.groups.filter(name='ADMIN').exists()
    )


@login_required
@user_passes_test(is_medico_recepcionista_o_enfermero)
def index (request):
    return render (request, 'index.html')

def login (request):
    
    return render(request, 'login.html')

@user_passes_test(is_medico_recepcionista_o_enfermero)
def dashboard (request):
    return render(request, 'dashboard.html') 

@user_passes_test(is_medico_admin_o_enfermero)
def areas (request):
    salas = Salas.objects.all()
    return render(request, 'areas.html',{'salas': salas}) 


@user_passes_test(is_medico_recepcionista_o_enfermero)
def calls (request):
    return render(request, 'calls.html') 

@user_passes_test(is_medico_admin_o_enfermero)
def pacientes (request):
    pacientess = Paciente.objects.all()
    return render(request, 'pacientes.html',{'pacientes':pacientess}) 

@user_passes_test(is_medico_admin_o_enfermero)
def agregar_paciente (request):
    if request.method == 'POST':
        dni = request.POST.get('dni')
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        direccion = request.POST.get('direccion')
        email = request.POST.get('email')
        obra_so = request.POST.get('obra_social')
        genero = request.POST.get('example-radio')
        telefono = request.POST.get('telefono')
        alergia = request.POST.get('alergia')
        enfermedad_cronica = request.POST.get('enf_cro')
        tratamiento_medico = request.POST.get('tratamiento')
        enfermedades_o_cirugias = request.POST.get('enf_cir')
        año_fecha_nac= request.POST.get('ano')
        dia_fecha_nac= request.POST.get('dia')
        mes_fecha_nac= request.POST.get('mes')
        enfermero_asic=request.POST.get('enfermero asignado')
        sala_asic=request.POST.get('zona paciente')
        internado = request.POST.get('internado-radio')

        fecha = año_fecha_nac + "-" + mes_fecha_nac + "-" + dia_fecha_nac
        
        if enfermero_asic is None: 
            enfe=None
        else:
            enfe=Enfermeros.objects.get(id=enfermero_asic)

        if sala_asic != None: 
            sala_pa=Salas.objects.get(id=sala_asic)

        if sala_asic is  None: 
            sala_pa=None
        
        email = request.POST.get('email')
        Paciente.objects.create(DNI=dni, nombre=nombre,apellido=apellido,direccion=direccion,email=email,obra_social=obra_so,fecha_nacimiento=fecha,genero=genero,telefono=telefono,alergia=alergia,enfermedad_cronica=enfermedad_cronica,tratamiento_medico=tratamiento_medico,enfermedades_o_cirugias=enfermedades_o_cirugias,enfermero=enfe,sala=sala_pa,internado=internado)

        return redirect('paciente')
    
    enferme = Enfermeros.objects.all()
    sala= Salas.objects.all()
    context = {'sala': sala, 'enfermeros': enferme}
    return render(request, 'agregar_pacientes.html', context)
     
@user_passes_test(is_medico_recepcionista_o_enfermero)
def perfil_paciente (request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)
    return render(request, 'perfil_paciente.html',{'paciente': paciente}) 

@user_passes_test(is_medico_recepcionista_o_enfermero)
def tabla_pacientes (request):
    return render(request, 'tabla_pacientes.html') 

@user_passes_test(is_medico_admin_o_enfermero)
def editar_paciente (request,paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)
    if request.method == 'POST':
        dni = request.POST.get('dni')
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        direccion = request.POST.get('direccion')
        email = request.POST.get('email')
        obra_so = request.POST.get('obra_social')
        genero = request.POST.get('example-radio')
        telefono = request.POST.get('telefono')
        alergia = request.POST.get('alergia')
        enfermedad_cronica = request.POST.get('enfermedad')
        tratamiento_medico = request.POST.get('tratamiento')
        enfermedades_o_cirugias = request.POST.get('enfermedades_cirugias')
        año_fecha_nac= request.POST.get('ano')
        dia_fecha_nac= request.POST.get('dia')
        mes_fecha_nac= request.POST.get('mes')
        enfermero_asic=request.POST.get('enfermero asignado')
        sala_asic=request.POST.get('zona paciente')
        internado = request.POST.get('internado-radio')
        
        if enfermero_asic is None: 
            enfe=None
        else:
            enfe=Enfermeros.objects.get(id=enfermero_asic)

        if sala_asic != None: 
            sala_pa=Salas.objects.get(id=sala_asic)

        if sala_asic is  None: 
            sala_pa=None
        
        fecha = año_fecha_nac + "-" + mes_fecha_nac + "-" + dia_fecha_nac

        email = request.POST.get('email')
        #actualizar
        paciente.DNI = dni
        paciente.nombre = nombre
        paciente.apellido = apellido
        paciente.direccion = direccion
        paciente.email = email
        paciente.obra_social = obra_so
        paciente.genero = genero
        paciente.telefono = telefono
        paciente.alergia = alergia
        paciente.enfermedad_cronica = enfermedad_cronica
        paciente.tratamiento_medico = tratamiento_medico
        paciente.enfermedades_o_cirugias = enfermedades_o_cirugias
        paciente.fecha_nacimiento = fecha
        paciente.internado = internado
        paciente.sala_id=sala_pa
        paciente.enfermero_id=enfe
        paciente.save()

        return redirect('perfil_paciente',paciente_id)

    enferme = Enfermeros.objects.all()
    sala= Salas.objects.all()    
    valores = {'sala': sala, 'enfermeros': enferme, 'paciente': paciente}
    return render(request, 'editar_paciente.html',valores) 

@user_passes_test(is_medico_admin)
def agregar_sala (request):
    return render(request, 'agregar_sala.html') 

@user_passes_test(is_admin)
def medicos (request):
    medicoss=Medico.objects.all()
    return render(request,'medicos.html',{'medicos':medicoss})

@user_passes_test(is_medico_admin)
def enfermeros (request):
    enfermeross=Enfermeros.objects.all()
    return render(request, 'enfermeros.html',{'enfermeros':enfermeross}) 

@user_passes_test(is_medico_admin)
def perfil_enfermero (request,enfermero_id):
    enfermeros=get_object_or_404(Enfermeros,id=enfermero_id)
    return render(request, 'perfil_enfermero.html',{'enfermeros': enfermeros})

@user_passes_test(is_admin)
def perfil_medico (request,medico_id):
    medicos=get_object_or_404(Medico,id=medico_id)
    return render(request, 'perfil_medico.html',{'medicos':medicos})

@user_passes_test(is_medico_admin)
def agregar_enfermero (request):
    if request.method == 'POST':
        dni = request.POST.get('dni')
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        direccion = request.POST.get('direccion')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')
        año_fecha_nac= request.POST.get('ano')
        dia_fecha_nac= request.POST.get('dia')
        mes_fecha_nac= request.POST.get('mes')
        fecha = año_fecha_nac + "-" + mes_fecha_nac + "-" + dia_fecha_nac
        genero = request.POST.get('example-radio')
        domingoMF = request.POST.get('DMF')
        domingoMI = request.POST.get('DMI')
        domingoTF = request.POST.get('DTF')
        domingoTI = request.POST.get('DTI')
        juevesMF = request.POST.get('JMF')
        juevesMI = request.POST.get('JMI')
        juevesTF = request.POST.get('JTF')
        juevesTI = request.POST.get('JTI')
        lunesMF = request.POST.get('LMI')
        lunesMI = request.POST.get('LMF')
        lunesTF = request.POST.get('LTF')
        lunesTI = request.POST.get('LTI')
        martesMF = request.POST.get('MMF')
        martesMI = request.POST.get('MMI')
        martesTF = request.POST.get('MTF')
        martesTI = request.POST.get('MTI')
        miercolesMF = request.POST.get('MMMF')
        miercolesMI = request.POST.get('MMMI')
        miercolesTF = request.POST.get('MMTF')
        miercolesTI = request.POST.get('MMTI')
        sabadoMF = request.POST.get('SMF')
        sabadoMI = request.POST.get('SMI')
        sabadoTF = request.POST.get('STF')
        sabadoTI = request.POST.get('STI')
        viernesMF = request.POST.get('VMF')
        viernesMI = request.POST.get('VMI')
        viernesTF = request.POST.get('VTF')
        viernesTI = request.POST.get('VTI')

        Enfermeros.objects.create(DNI=dni,nombre=nombre,apellido=apellido,direccion=direccion,email=email,fecha_nacimiento=fecha,genero=genero,telefono=telefono,domingoMF=domingoMF,domingoMI=domingoMI,domingoTF=domingoTF,domingoTI=domingoTI,juevesMF=juevesMF,juevesMI=juevesMI,juevesTF=juevesTF,juevesTI=juevesTI,lunesMF=lunesMF,lunesMI=lunesMI,lunesTF=lunesTF,lunesTI=lunesTI,martesMF=martesMF,martesMI=martesMI,martesTF=martesTF,martesTI=martesTI,miercolesMF=miercolesMF,miercolesMI=miercolesMI,miercolesTF=miercolesTF,miercolesTI=miercolesTI,sabadoMF=sabadoMF,sabadoMI=sabadoMI,sabadoTF=sabadoTF,sabadoTI=sabadoTI,viernesMF=viernesMF,viernesMI=viernesMI,viernesTF=viernesTF,viernesTI=viernesTI)
        return redirect ('enfermeros')

    return render(request, 'agregar_enfermero.html') 

@user_passes_test(is_admin)
def agregar_medico (request):
   if request.method == 'POST':
        dni = request.POST.get('dni')
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        direccion = request.POST.get('direccion')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')
        año_fecha_nac= request.POST.get('ano')
        dia_fecha_nac= request.POST.get('dia')
        mes_fecha_nac= request.POST.get('mes')
        matricula=request.POST.get('matricula')
        fecha = año_fecha_nac + "-" + mes_fecha_nac + "-" + dia_fecha_nac
        genero = request.POST.get('example-radio')
        especialidad=request.POST.get('especialidad')
        domingoMF = request.POST.get('DMF')
        domingoMI = request.POST.get('DMI')
        domingoTF = request.POST.get('DTF')
        domingoTI = request.POST.get('DTI')
        juevesMF = request.POST.get('JMF')
        juevesMI = request.POST.get('JMI')
        juevesTF = request.POST.get('JTF')
        juevesTI = request.POST.get('JTI')
        lunesMF = request.POST.get('LMI')
        lunesMI = request.POST.get('LMF')
        lunesTF = request.POST.get('LTF')
        lunesTI = request.POST.get('LTI')
        martesMF = request.POST.get('MMF')
        martesMI = request.POST.get('MMI')
        martesTF = request.POST.get('MTF')
        martesTI = request.POST.get('MTI')
        miercolesMF = request.POST.get('MMMF')
        miercolesMI = request.POST.get('MMMI')
        miercolesTF = request.POST.get('MMTF')
        miercolesTI = request.POST.get('MMTI')
        sabadoMF = request.POST.get('SMF')
        sabadoMI = request.POST.get('SMI')
        sabadoTF = request.POST.get('STF')
        sabadoTI = request.POST.get('STI')
        viernesMF = request.POST.get('VMF')
        viernesMI = request.POST.get('VMI')
        viernesTF = request.POST.get('VTF')
        viernesTI = request.POST.get('VTI')

        Medico.objects.create(DNI=dni,nombre=nombre,matricula=matricula,apellido=apellido,direccion=direccion,email=email,especialidad=especialidad,fecha_nacimiento=fecha,genero=genero,telefono=telefono,domingoMF=domingoMF,domingoMI=domingoMI,domingoTF=domingoTF,domingoTI=domingoTI,juevesMF=juevesMF,juevesMI=juevesMI,juevesTF=juevesTF,juevesTI=juevesTI,lunesMF=lunesMF,lunesMI=lunesMI,lunesTF=lunesTF,lunesTI=lunesTI,martesMF=martesMF,martesMI=martesMI,martesTF=martesTF,martesTI=martesTI,miercolesMF=miercolesMF,miercolesMI=miercolesMI,miercolesTF=miercolesTF,miercolesTI=miercolesTI,sabadoMF=sabadoMF,sabadoMI=sabadoMI,sabadoTF=sabadoTF,sabadoTI=sabadoTI,viernesMF=viernesMF,viernesMI=viernesMI,viernesTF=viernesTF,viernesTI=viernesTI)
        return redirect('medicos')
   
   return render(request, 'agregar_medico.html') 

@user_passes_test(is_medico_admin)
def editar_enfermero (request,enfermero_id):
    enfermeros=get_object_or_404(Enfermeros,id=enfermero_id)
    if request.method == 'POST':
        dni = request.POST.get('dni')
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        direccion = request.POST.get('direccion')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')
        año_fecha_nac= request.POST.get('ano')
        dia_fecha_nac= request.POST.get('dia')
        mes_fecha_nac= request.POST.get('mes')
        fecha = año_fecha_nac + "-" + mes_fecha_nac + "-" + dia_fecha_nac
        genero = request.POST.get('example-radio')
        domingoMF = request.POST.get('DMF')
        domingoMI = request.POST.get('DMI')
        domingoTF = request.POST.get('DTF')
        domingoTI = request.POST.get('DTI')
        juevesMF = request.POST.get('JMF')
        juevesMI = request.POST.get('JMI')
        juevesTF = request.POST.get('JTF')
        juevesTI = request.POST.get('JTI')
        lunesMF = request.POST.get('LMF')
        lunesMI = request.POST.get('LMI')
        lunesTF = request.POST.get('LTF')
        lunesTI = request.POST.get('LTI')
        martesMF = request.POST.get('MMF')
        martesMI = request.POST.get('MMI')
        martesTF = request.POST.get('MTF')
        martesTI = request.POST.get('MTI')
        miercolesMF = request.POST.get('MMMF')
        miercolesMI = request.POST.get('MMMI')
        miercolesTF = request.POST.get('MMTF')
        miercolesTI = request.POST.get('MMTI')
        sabadoMF = request.POST.get('SMF')
        sabadoMI = request.POST.get('SMI')
        sabadoTF = request.POST.get('STF')
        sabadoTI = request.POST.get('STI')
        viernesMF = request.POST.get('VMF')
        viernesMI = request.POST.get('VMI')
        viernesTF = request.POST.get('VTF')
        viernesTI = request.POST.get('VTI')

        enfermeros.DNI=dni
        enfermeros.nombre=nombre
        enfermeros.apellido=apellido
        enfermeros.direccion=direccion
        enfermeros.email=email
        enfermeros.fecha_nacimiento=fecha
        enfermeros.telefono=telefono
        enfermeros.genero=genero
        enfermeros.domingoMI=domingoMI
        enfermeros.domingoMF=domingoMF
        enfermeros.domingoTF=domingoTF
        enfermeros.domingoTI=domingoTI
        enfermeros.lunesMI=lunesMI
        enfermeros.lunesMF=lunesMF
        enfermeros.lunesTF=lunesTF
        enfermeros.lunesTI=lunesTI
        enfermeros.martesMI=martesMI
        enfermeros.martesMF=martesMF
        enfermeros.martesTF=martesTF
        enfermeros.martesTI=martesTI
        enfermeros.miercolesMI=miercolesMI
        enfermeros.miercolesMF=miercolesMF
        enfermeros.miercolesTF=miercolesTF
        enfermeros.miercolesTI=miercolesTI
        enfermeros.juevesMI=juevesMI
        enfermeros.juevesMF=juevesMF
        enfermeros.juevesTF=juevesTF
        enfermeros.juevesTI=juevesTI
        enfermeros.viernesMI=viernesMI
        enfermeros.viernesMF=viernesMF
        enfermeros.viernesTF=viernesTF
        enfermeros.viernesTI=viernesTI
        enfermeros.sabadoMI=sabadoMI
        enfermeros.sabadoMF=sabadoMF
        enfermeros.sabadoTF=sabadoTF
        enfermeros.sabadoTI=sabadoTI
        enfermeros.save()

        return redirect('perfil_enfermero',enfermero_id)

    return render(request, 'editar_enfermero.html',{'enfermeros': enfermeros}) 

@user_passes_test(is_admin)
def editar_medico (request,medico_id):
    medicos=get_object_or_404(Medico,id=medico_id)
    if request.method == 'POST':
        dni = request.POST.get('dni')
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        direccion = request.POST.get('direccion')
        email = request.POST.get('email')
        matricula=request.POST.get('matricula')
        telefono = request.POST.get('telefono')
        año_fecha_nac= request.POST.get('ano')
        dia_fecha_nac= request.POST.get('dia')
        mes_fecha_nac= request.POST.get('mes')
        fecha = año_fecha_nac + "-" + mes_fecha_nac + "-" + dia_fecha_nac
        genero = request.POST.get('example-radio')
        especialidad=request.POST.get('especialidad')
        domingoMF = request.POST.get('DMF')
        domingoMI = request.POST.get('DMI')
        domingoTF = request.POST.get('DTF')
        domingoTI = request.POST.get('DTI')
        juevesMF = request.POST.get('JMF')
        juevesMI = request.POST.get('JMI')
        juevesTF = request.POST.get('JTF')
        juevesTI = request.POST.get('JTI')
        lunesMF = request.POST.get('LMF')
        lunesMI = request.POST.get('LMI')
        lunesTF = request.POST.get('LTF')
        lunesTI = request.POST.get('LTI')
        martesMF = request.POST.get('MMF')
        martesMI = request.POST.get('MMI')
        martesTF = request.POST.get('MTF')
        martesTI = request.POST.get('MTI')
        miercolesMF = request.POST.get('MMMF')
        miercolesMI = request.POST.get('MMMI')
        miercolesTF = request.POST.get('MMTF')
        miercolesTI = request.POST.get('MMTI')
        sabadoMF = request.POST.get('SMF')
        sabadoMI = request.POST.get('SMI')
        sabadoTF = request.POST.get('STF')
        sabadoTI = request.POST.get('STI')
        viernesMF = request.POST.get('VMF')
        viernesMI = request.POST.get('VMI')
        viernesTF = request.POST.get('VTF')
        viernesTI = request.POST.get('VTI')

        medicos.DNI=dni
        medicos.nombre=nombre
        medicos.apellido=apellido
        medicos.direccion=direccion
        medicos.email=email
        medicos.fecha_nacimiento=fecha
        medicos.telefono=telefono
        medicos.genero=genero
        medicos.especialidad=especialidad
        medicos.matricula=matricula
        medicos.domingoMI=domingoMI
        medicos.domingoMF=domingoMF
        medicos.domingoTF=domingoTF
        medicos.domingoTI=domingoTI
        medicos.lunesMI=lunesMI
        medicos.lunesMF=lunesMF
        medicos.lunesTF=lunesTF
        medicos.lunesTI=lunesTI
        medicos.martesMI=martesMI
        medicos.martesMF=martesMF
        medicos.martesTF=martesTF
        medicos.martesTI=martesTI
        medicos.miercolesMI=miercolesMI
        medicos.miercolesMF=miercolesMF
        medicos.miercolesTF=miercolesTF
        medicos.miercolesTI=miercolesTI
        medicos.juevesMI=juevesMI
        medicos.juevesMF=juevesMF
        medicos.juevesTF=juevesTF
        medicos.juevesTI=juevesTI
        medicos.viernesMI=viernesMI
        medicos.viernesMF=viernesMF
        medicos.viernesTF=viernesTF
        medicos.viernesTI=viernesTI
        medicos.sabadoMI=sabadoMI
        medicos.sabadoMF=sabadoMF
        medicos.sabadoTF=sabadoTF
        medicos.sabadoTI=sabadoTI
        medicos.save()

        return redirect('perfil_medico',medico_id)

    return render(request, 'editar_medico.html',{'medicos':medicos})


def contar_llamados(request):
    cantidad_de_registros = Llamados.objects.all().count()
    return render(request, 'dashboard.html', {'cantidad_de_registros': cantidad_de_registros})


@user_passes_test(is_admin)
def users (request):
    users = User.objects.all()
    return render(request, 'users.html',{'users': users})

@user_passes_test(is_admin)
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

@user_passes_test(is_medico_recepcionista_o_enfermero)
def historial_clinico (request,paciente_id):
    try:
        pacientes=get_object_or_404(Paciente,id=paciente_id)

        llamadas = Llamados.objects.filter(id_paciente=pacientes)

        return render(request, 'historial_clinico.html',{'pacientes':pacientes , 'llamadas':llamadas})  

    except Paciente.DoesNotExist:
        # Manejar el caso en el que el paciente no existe
        return redirect('pacientes')

@user_passes_test(is_medico_recepcionista_o_enfermero)
def historial_llamadas (request):
    llamadas=Llamados.objects.all()
    return render(request, 'historial_llamadas.html',{'llamadas':llamadas})  

@user_passes_test(is_medico_recepcionista_o_enfermero)
def atender_calls (request):
    return render(request, 'atender_calls.html')  

@user_passes_test(is_medico_recepcionista_o_enfermero)
def agregar_llamadas (request):
    if request.method == 'POST':
        tipo_llamado= request.POST.get('triage')
        id_paciente = request.POST.get('dni')
        ubicacion=request.POST.get('ubicacion')
        id_zona=request.POST.get('Sala')
        id_medico=None
        estado=False
        
        if ubicacion is None:
            ubi=None
        else:
            ubi=request.POST.get('ubicacion')
        
        if id_zona != None: 
            zona=Salas.objects.get(id=id_zona)

        if id_zona is  None: 
            zona=None
        
        
        Llamados.objects.create(tipo_llamado=tipo_llamado, ubicacion=ubi, id_paciente=id_paciente, id_zona=zona,id_medico=id_medico,estado=estado )
        
        return redirect('calls')
    
    pacientes = Paciente.objects.all()
    salas = Salas.objects.all()
    return render(request, 'agregar_llamadas.html',{'pacientes' : pacientes,'salas' : salas})  

@user_passes_test(is_medico_admin)
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

@user_passes_test(is_medico_admin)
def procesar_formulario(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        tipo = request.POST.get('select_salas')

        Salas.objects.create(nombre=nombre, tipo_sala=tipo)

        return redirect('areas')  # Reemplaza 'lista_salas' con la URL correcta

    return render(request, 'agregar_sala.html')

@user_passes_test(is_admin)
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

@user_passes_test(is_admin)
def eliminar_objeto(request,modelo ,objeto_id):
    if modelo == "User":

        objeto_a_eliminar = get_object_or_404(User, id=objeto_id)
        objeto_a_eliminar.delete()

        return redirect('users')  # Redirige a donde desees después de eliminar el objeto
    
    elif modelo == "Salas":

        objeto_a_eliminar = get_object_or_404(Salas, id=objeto_id)
        objeto_a_eliminar.delete()

        return redirect('areas')  # Redirige a donde desees después de eliminar el objeto
    
    elif modelo == "Enfermeros":

        objeto_a_eliminar = get_object_or_404(Enfermeros, id=objeto_id)
        objeto_a_eliminar.delete()

        return redirect('enfermeros')  # Redirige a donde desees después de eliminar el objeto
    
    elif modelo == "Paciente":

        objeto_a_eliminar = get_object_or_404(Paciente, id=objeto_id)
        objeto_a_eliminar.delete()

        return redirect('paciente')  # Redirige a donde desees después de eliminar el objeto

    elif modelo == "Medico":

        objeto_a_eliminar = get_object_or_404(Medico, id=objeto_id)
        objeto_a_eliminar.delete()

        return redirect('medicos')  # Redirige a donde desees después de eliminar el objeto

    elif modelo == "Llamados":

        objeto_a_eliminar = get_object_or_404(Llamados, id=objeto_id)
        objeto_a_eliminar.delete()

        return redirect('calls')  # Redirige a donde desees después de eliminar el objeto


@user_passes_test(is_admin)
def agregar_users(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            role = form.cleaned_data['role']
            grupo = Group.objects.get(name=role)
            user.groups.add(grupo)
            login(request, user, role)
            return redirect('user')  # Redirige al inicio después del registro
    else:
        form = RegistrationForm()
    return render(request, 'agregar_users.html', {'form': form})




    