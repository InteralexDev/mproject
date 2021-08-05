from django import forms
from .models import Task

# Classe formulaire permet de gerer les formulaires directement via les modèles

class DeveloperForm(forms.ModelForm):
    class Meta: 
        model = Task
        fields = ['title', 'description']