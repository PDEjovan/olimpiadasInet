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
]