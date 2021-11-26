from rest_framework.serializers import ModelSerializer

from users.models import User


# Default
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'profile_image_url', 'birth_date', 'last_login', 'is_staff']


# Create
class CreateUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email', 'profile_image_url', 'birth_date', 'is_staff']

