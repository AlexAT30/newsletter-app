from rest_framework.viewsets import ModelViewSet 
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from users.models import User
#Serializers:
from users.serializers import UserSerializer

class UsersViewSet(ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  permission_classes = (IsAuthenticatedOrReadOnly)
