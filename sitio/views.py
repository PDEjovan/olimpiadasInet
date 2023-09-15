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

<<<<<<< HEAD

=======
def calls (request):
    return render(request, 'calls.html') 
>>>>>>> ad8b05ee93eed7f89d0652f55199327fd3567549
