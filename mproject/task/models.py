from django.db import models
from django.apps import apps
from developer.models import Developer

class Task(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    assignee = models.ForeignKey(Developer, related_name="tasks", on_delete=models.SET_NULL, null=True, verbose_name="assignee")

    def is_free(self):
        return self.assignee == "NULL"

    def __str__(self): 
        return f"{self.title} ({self.description})"