from django import forms
from .models import Developer

# Classe formulaire permet de gerer les formulaires directement via les modèles

class DeveloperForm(forms.ModelForm):
    class Meta: 
        model = Developer 
        fields = ['first_name', 'last_name']