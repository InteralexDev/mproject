from django.urls import path

# Import de views.py
from . import views
from .views import IndexView, TaskDetailVue

app_name = 'task'

urlpatterns = [
    path('', IndexView.as_view(), name='index'), 
    path('<int:pk>', TaskDetailVue.as_view(), name='detail'),
    path('create', views.create, name='create'),
    path('delete/<int:id>', views.delete, name='delete'),
]