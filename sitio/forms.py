from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile

class RegistrationForm(UserCreationForm):
    role = forms.ChoiceField(choices=UserProfile.role_choices)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'role']