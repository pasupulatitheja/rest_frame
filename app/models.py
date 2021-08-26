from django.db import models

# Create your models here.
class EmployeeModel(models.Model):
    emid = models.IntegerField(primary_key=True)
    ename = models.CharField(max_length=30)
    esalary = models.FloatField()
    eaddress = models.CharField(max_length=30)

