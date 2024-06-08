from django.db import models
from django.core.validators import RegexValidator


# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=200, unique=True)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name + " - " + self.location

class Employee(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    profession = models.CharField(max_length=200)
    department = models.ForeignKey(Department, to_field="name", on_delete=models.CASCADE, related_name="employees")

    def __str__(self):
        return self.first_name + " - " + self.last_name



