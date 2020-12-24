from django.db import models

# Create your models here.

class Employee(models.Model) :
    eno=models.IntegerField()
    ename=models.CharField(max_length=40)
    esal=models.IntegerField()
    eaddr=models.CharField(max_length=50)