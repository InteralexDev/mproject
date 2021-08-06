# Imports relatifs au librairies
from django.apps import AppConfig

# Cette classe défini l'application
# elle est appellée dans le settings.py via INSTALLED_APPS
class DeveloperConfig(AppConfig):
    name = 'developer'
