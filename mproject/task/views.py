from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Task

class IndexView(ListView): 
    model = Task
    template_name = "task/index.html" 
    context_object_name = 'tasks'
