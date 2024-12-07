from django.db import models

# Create your models here.

class Attendance(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    level = models.IntegerField()
    contact = models.CharField(max_length=100)