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
    path('calls/', views.calls),
    
]