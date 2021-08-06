# Imports relatifs au librairies
from django import forms

# Imports relatifs au modèles
from .models import Developer

# Classe formulaire permet de gerer les formulaires directement via les modèles
class DeveloperForm(forms.ModelForm):
    class Meta: 
        model = Developer 
        fields = ['first_name', 'last_name']