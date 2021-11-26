from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.viewsets import ModelViewSet
from tags.models import Tag
from tags.serializers import CreateTagSerializer, TagSerializer

class TagsViewSet(ModelViewSet):
  queryset = Tag.objects.all()
  serializer_class = CreateTagSerializer

  def get_serializer_class(self):
    if self.action == 'list' or self.action == 'retrieve':
      return TagSerializer
    return self.serializer_class

  def get_permissions(self):
    if self.action == 'create' or self.action == 'update' or self.action == 'parcial_update' or 'destroy':
      permission_classes = [IsAdminUser]
    else:
      permission_classes = [AllowAny]
    return [permission() for permission in permission_classes]