from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE, related_name= "profile")
    phone_number = models.CharField(max_length=25, unique=True, validators=[RegexValidator(r"^\+(?:[0-9] ?){6,14}[0-9]$")])
    language_preferences = models.CharField(max_length= 35)

