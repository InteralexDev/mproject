from django.urls import path
#import locaux
from . import views
from .views import DevDetailVue, IndexView

app_name = 'developer'

# Les urls de l'application :
#   '' = /developer (car on est ici dans l'application developer)
#   '<int:developer_id>' = /developer/<int:developer_id>
urlpatterns = [
    path('', IndexView.as_view(), name='index'), 
    path('<int:pk>', DevDetailVue.as_view(), name='detail'),
    path('create', views.create, name='create'),
]
