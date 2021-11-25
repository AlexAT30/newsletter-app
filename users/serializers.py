from rest_framework.serializers import ModelSerializer

from users.models import User


# get (list) and not admin
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'profile_image_url', 'birth_date', 'last_login']


# post
class CrearUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email', 'profile_image_url', 'is_staff']


# retrieve and admin /
class DetalleUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
