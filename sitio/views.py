from django.shortcuts import render
from .models import User
# Create your views here.
def index (request):
    user=User.objects.all()
    return render (request, 'index.html', {
        'user': user
    })


def login (request):
    return render(request, 'login.html') 

def dashboard (request):
    return render(request, 'dashboard.html') 

def areas (request):
    return render(request, 'areas.html') 