from django.urls import path

# Import de views.py
from . import views
from .views import IndexView

app_name = 'task'

urlpatterns = [
    path('', IndexView.as_view(), name='index'), 
]