from django.db import models

# Create your models here.

class Attendant(models.Model):
    name = models.CharField(max_length=50)
    department = models.CharField(max_length=100)
    # level = models.Integers()
    # nat