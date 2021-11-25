from rest_framework.viewsets import ModelViewSet 
from users.models import User
from users.serializers import UserSerializer
#Serializers:

class UsersViewSet(ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer
