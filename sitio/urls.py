from . import views
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView,logout_then_login
from django.contrib.auth.decorators import login_required
urlpatterns = [ 
    path('',login_required(views.calls),name='calls'),  
    path('dashboard/',login_required(views.dashboard),name='dashboard'),

    path('accounts/login/',LoginView.as_view(template_name='login.html'),name='login'),

    path('logout/',logout_then_login,name='logout'),

    path('areas/', login_required(views.areas),name='areas'),
    path('agregar_sala/', login_required(views.agregar_sala)),
    path('editar_sala/<int:sala_id>/', login_required(views.editar_sala),name='editar_sala'),
    path('procesar_formulario/', login_required(views.procesar_formulario), name='procesar_formulario'),

    path('pacientes/', login_required(views.pacientes),name ='paciente'),
    path('agregar_paciente/',login_required(views.agregar_paciente),name='agregar_paciente'),
    path('editar_paciente/<int:paciente_id>/',login_required(views.editar_paciente),name='editar_paciente'),
    path('perfil_paciente/<int:paciente_id>/',login_required(views.perfil_paciente),name='perfil_paciente'),
    path('tabla_pacientes/',login_required(views.tabla_pacientes),name='tabla_pacientes'),

    path('enfermeros/',login_required(views.enfermeros),name='enfermeros'),
    path('perfil_enfermero/<int:enfermero_id>/',login_required(views.perfil_enfermero),name='perfil_enfermero'),
    path('agregar_enfermero/',login_required(views.agregar_enfermero),name='agregar_enfermero'),
    path('editar_enfermero/<int:enfermero_id>/',login_required(views.editar_enfermero),name='editar_enfermero'),

    path('medicos/',login_required(views.medicos),name='medicos'),
    path('perfil_medico/<int:medico_id>/',login_required(views.perfil_medico),name='perfil_medico'),
    path('agregar_medico/',login_required(views.agregar_medico),name='agregar_medico'),
    path('editar_medico/<int:medico_id>/',login_required(views.editar_medico),name='editar_medico'),

    path('users/',login_required(views.users),name='users'),
    path('editar_users/<int:user_id>/',login_required(views.editar_users),name='editar_users'),
    path('agregar_users/',login_required(views.agregar_users),name='agregar_users'),
    path('procesar_formulario_users/', login_required(views.procesar_formulario_users), name='procesar_formulario_users'),

    path('historial_clinico/<int:paciente_id>/',login_required(views.historial_clinico),name='historial_clinico'),
    path('historial_llamadas/',login_required(views.historial_llamadas),name='historial_llamadas'),

    path('agregar_llamadas/',login_required(views.agregar_llamadas),name='agregar_llamadas'),
    path('calls/', login_required(views.calls),name='calls'),
    path('atender_calls/',login_required(views.atender_calls),name='atender_calls'),

    path('eliminar_objeto/<modelo>/<int:objeto_id>/',login_required(views.eliminar_objeto), name='eliminar_objeto'),


]