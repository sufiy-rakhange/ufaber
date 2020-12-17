from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    discription = models.TextField(blank=False, null=False)
    duration = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return f"{self.title}"

class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=False, null=False)
    discription = models.TextField(blank=False, null=False)
    startdate = models.DateField()
    enddate = models.DateField()

    def __str__(self):
        return f"{self.title}"
