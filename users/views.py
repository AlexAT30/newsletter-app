from copy import copy
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import action
# Models #
from users.models import User
from newsletters.models import Newsletter
#Serializers:
from users.serializers import UserSerializer, CreateUserSerializer
from newsletters.serializers import ToUsersNewsletterSerializer 

class UsersViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = CreateUserSerializer
  permission_classes = [AllowAny]

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

  def update(self, request, pk=None):
    # Verification to the user is admin or the current user #
    if not request.user.id == pk:
      if not request.user.is_staff: 
        return Response(
          status=status.HTTP_401_UNAUTHORIZED,
          data={'error': 'You don\'t have permission to do this.'}
        )

    data = copy(request.data)
    serializer_class = self.get_serializer_class()
    serialized = serializer_class(data=data)
    if not serialized.is_valid():
      return Response(
        status=status.HTTP_400_BAD_REQUEST,
        data=serialized.errors
      )
    user = User(**data)
    user.id = pk
    user.save(force_update=True)
    self.encrypt_password(data)

    return Response(
      status=status.HTTP_201_CREATED,
      data={'message': 'User updated correctly'}
    )

  def destroy(self, request, pk=None):
    # Verification to the user is admin or the current user #
    if not request.user.id == pk:
      if not request.user.is_staff: 
        return Response(
          status=status.HTTP_401_UNAUTHORIZED,
          data={'error': 'You don\'t have permission to do this.'}
        )
  
    user = User.objects.get(id=pk)
    user.is_active = False
    user.save(force_update=True)

    return Response(
      status=status.HTTP_201_CREATED,
      data={'message': 'User deactivated correctly'}
    )

  def partial_update(self):
    return Response(
      status=status.HTTP_404_NOT_FOUND,
      data={'error': 'method no available'}
    )

  @action(methods=['GET'], detail=True)
  def newsletters(self, request, pk=None):
    serializer_class = self.get_serializer_class()
    #Likes
    liked_data = Newsletter.objects.filter(likes=pk)
    liked_serialized = serializer_class(data=liked_data, many=True)
    liked_serialized.is_valid()
    #Subscribes
    subscribed_data = Newsletter.objects.filter(subscribed_users=pk)
    subscribed_serialized = serializer_class(data=subscribed_data, many=True)
    subscribed_serialized.is_valid()
    if not request.user.is_staff:
      return Response(
      status=status.HTTP_200_OK,
      data={
        'liked': liked_serialized.data,
        'subscribed': subscribed_serialized.data
      }
    )
    #Created (only for admins)
    created_data = Newsletter.objects.filter(created_by=pk)
    created_serialized = serializer_class(data=created_data, many=True)
    created_serialized.is_valid()
    return Response(
      status=status.HTTP_200_OK,
      data={
        'liked': liked_serialized.data,
        'subscribed': subscribed_serialized.data,
        'created': created_serialized.data
      }
    )

  def encrypt_password(self, data):
    user = User.objects.get(username=data['username'])
    user.set_password(data['password'])
    User.save(user, force_update=True)

  def get_serializer_class(self):
    if self.action == 'list' or self.action == 'retrieve':
      return UserSerializer
    if self.action == 'newsletters':
      return ToUsersNewsletterSerializer
    return self.serializer_class

  def get_permissions(self):
    if self.action == 'newsletters' or self.action == 'update' or self.action == 'destroy':
      permission_classes = [IsAuthenticated]
    else:
      permission_classes = [AllowAny]
    return [permission() for permission in permission_classes]
  