from copy import copy, error
from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet 
from users.models import User
#Serializers:
from users.serializers import UserSerializer
from users.serializers import CreateUserSerializer

class UsersViewSet(ModelViewSet):
  queryset = User.objects.all()
  serializer_class = CreateUserSerializer

  def create(self, request):
    data = copy(request.data)
    serializer_class = self.get_serializer_class()
    serialized = serializer_class(data=data)
    
    if not serialized.is_valid():
      return Response(
        status = status.HTTP_400_BAD_REQUEST,
        data = serialized.errors
      )
    serialized.save()
    self.encrypt_password(data) # <- This function is used to encrypt the password 
    
    return Response(
      status = status.HTTP_200_OK,
      data = serialized.data
    )
  #Falta agregar la encriptacion de contraseña en update y parcial_update

  def encrypt_password(self, data):
    user = User.objects.get(username=data['username'])
    user.set_password(data['password'])
    User.save(user, force_update=True)

  def get_serializer_class(self):
    if self.action == 'list' or self.action == 'retrieve':
      return UserSerializer

    return self.serializer_class

  