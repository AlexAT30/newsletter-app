from copy import copy
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from newsletters.models import Newsletter
from users.models import User
from rest_framework.decorators import action
#Serializers:
from users.serializers import UserSerializer, CreateUserSerializer
from newsletters.serializers import NewsletterSerializer 

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
      status = status.HTTP_201_CREATED,
      data = {'message': 'User created correctly'}
    )
  #Falta agregar la encriptacion de contraseña en update y parcial_update

  @action(methods=['GET'], detail=True)
  def newsletters(self, request, pk=None):
    data = Newsletter.objects.filter(created_by=pk)
    serialized = NewsletterSerializer(data=data, many=True)
    serialized.is_valid()
    return Response(
      status=status.HTTP_202_ACCEPTED,
      data=serialized.data
    )

  def encrypt_password(self, data):
    user = User.objects.get(username=data['username'])
    user.set_password(data['password'])
    User.save(user, force_update=True)

  def get_serializer_class(self):
    if self.action == 'list' or self.action == 'retrieve':
      return UserSerializer
    return self.serializer_class

  