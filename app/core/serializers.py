from rest_framework import serializers
from .models import Password
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password"]
        extra_kwargs= {
            "password":{"write_only": True}
        }

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User.objects.create(**validated_data)
        user.set_password(password) # Applies hashing
        user.save()
        return user

class PasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Password
        fields = ["user", "website", "username", "password"]
        extra_kwargs = {
            "user": {"write_only" : True}
        }
