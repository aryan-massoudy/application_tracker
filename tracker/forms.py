# tracker/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Application

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['company_name', 'position', 'application_date', 'status', 'notes', 'application_link', 'contact_email']
        widgets = {
            'application_date': forms.DateInput(attrs={'type': 'date'}),
        }