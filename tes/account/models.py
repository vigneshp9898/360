from django.db import models

# Create your models here.
class Contacr(models.Model):
    name = models.CharField(max_length=50)
    email= models.EmailField()
    designation = models.CharField(max_length=50)
    emp_id = models.CharField(max_length=50)
