from django.db import models

# Create your models here.


class Employee(models.Model):
    eid=models.CharField(max_length=200)
    ename=models.CharField(max_length=200)
    eemail=models.EmailField(max_length=100)
    econtact=models.CharField(max_length=15)

