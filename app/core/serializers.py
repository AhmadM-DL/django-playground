from rest_framework import serializers
from .models import Password
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password"]
        extra_kwargs= {
            "password":{"write_only": True}
            }

class CreatePasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Password
        fields = ["user", "website", "username", "password"]

class PasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Password
        fields = ["website", "username", "password"]
