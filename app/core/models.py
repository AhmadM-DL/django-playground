from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Password(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE, related_name="passwords")
    website = models.CharField(max_length=100)
    username =  models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.website + "-" + self.username