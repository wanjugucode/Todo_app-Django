from django.db import models

# Create your models here.

class Task(models.Model):
    task_title=models.CharField(max_length=20)
    task_duration=models.CharField(max_length=12)
    day=models.CharField(max_length=12)
    task_status=models.CharField(max_length=12)

