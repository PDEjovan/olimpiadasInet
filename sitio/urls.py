from . import views
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView,logout_then_login
from django.contrib.auth.decorators import login_required
urlpatterns = [ 
    path('',login_required(views.index),name='index'),  
    path('dashboard/',login_required(views.dashboard),name='dashboard'),
    path('accounts/login/',LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/',logout_then_login,name='logout'),
    path('calls/', login_required(views.calls)),
    path('pacientes/', login_required(views.pacientes)),
    path('areas/', login_required(views.areas),name='areas'),
    path('agregar_sala/', login_required(views.agregar_sala)),
    path('editar_sala/<int:sala_id>/', login_required(views.editar_sala),name='editar_sala'),
    path('procesar_formulario/', login_required(views.procesar_formulario), name='procesar_formulario'),
    path('agregar_paciente/',login_required(views.agregar_paciente),name='agregar_paciente'),
    path('editar_paciente/',login_required(views.editar_paciente),name='editar_paciente'),
    path('perfil_paciente/',login_required(views.perfil_paciente),name='perfil_paciente'),
    path('tabla_pacientes/',login_required(views.tabla_pacientes),name='tabla_pacientes'),
    path('medicos/',login_required(views.medicos),name='medicos'),
    path('enfermeros/',login_required(views.enfermeros),name='enfermeros'),
    path('perfil_enfermero/',login_required(views.perfil_enfermero),name='perfil_enfermero'),
    path('perfil_medico/',login_required(views.perfil_medico),name='perfil_medico'),
    path('agregar_medico/',login_required(views.agregar_medico),name='agregar_medico'),
    path('agregar_enfermero/',login_required(views.agregar_enfermero),name='agregar_enfermero'),
    path('editar_medico/',login_required(views.editar_medico),name='editar_medico'),
    path('editar_enfermero/',login_required(views.editar_enfermero),name='editar_enfermero'),
    path('users/',login_required(views.users),name='users'),
    path('editar_users/',login_required(views.editar_users),name='editar_users'),
    path('agregar_users/',login_required(views.agregar_users),name='agregar_users'),
    path('historial_clinico/',login_required(views.historial_clinico),name='historial_clinico'),
    path('historial_llamadas/',login_required(views.historial_llamadas),name='historial_llamadas'),
]