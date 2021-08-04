from django.urls import path
from . import views

app_name = 'developer'

# Les urls de l'application :
#   '' = /developer (car on est ici dans l'application developer)
#   'specifics/<int:developer_id>' = /developer/specifics/<int:developer_id>
urlpatterns = [
    path('', views.index, name='index'),
    path('specifics/<int:developer_id>', views.detail, name='detail'), 
]
