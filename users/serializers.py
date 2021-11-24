from rest_framework.serializers import ModelSerializer

"""
from users.models import User


# get (list) and not admin
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'img']


# post
class CrearUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


# retrieve and admin /
class DetalleUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

"""