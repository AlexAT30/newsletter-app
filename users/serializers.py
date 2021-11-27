from django.contrib.auth import models
from rest_framework import fields
from rest_framework.serializers import ModelSerializer

from users.models import User


# Default
class UserSerializer(ModelSerializer):
  class Meta:
    model = User
    fields = ['id', 'username', 'first_name', 'last_name', 'email', 'profile_image_url', 'last_login', 'is_staff', 'is_active']

# Create
class CreateUserSerializer(ModelSerializer):
  class Meta:
    model = User
    fields = ['username', 'password', 'first_name', 'last_name', 'email', 'profile_image_url', 'is_staff']

# Newsletters
class MinimalUserSerializer(ModelSerializer):
  class Meta:
    model = User
    fields = ['id', 'username', 'email', 'profile_image_url']


