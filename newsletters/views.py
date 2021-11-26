from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import  IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly
from copy import copy
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response
from newsletters.models import Newsletter
from newsletters.serializers import CreateNewsletterSerializer, NewsletterSerializer


class NewslettersViewSet(ModelViewSet):
  queryset = Newsletter.objects.all()
  serializer_class = CreateNewsletterSerializer

  def create(self, request):
    data = copy(request.data)
    data['created_by'] = request.user.id
    serializer_class = self.get_serializer_class()
    serialized = serializer_class(data=data)

    if not serialized.is_valid():
      return Response(
        status = status.HTTP_400_BAD_REQUEST,
        data = serialized.errors
      )
    serialized.save()
    return Response(
      status = status.HTTP_201_CREATED,
      data = {'message': 'Newsletter created correctly'}
    )

  @action(methods=['POST'], detail=True)
  def like(self, request, pk=None):
    data = Newsletter.objects.get(id=pk)
    is_liked = False
    try:
      data.likes.get(id=request.user.id)
      is_liked = True
    except:
      pass
    if is_liked:
      data.likes.remove(request.user.id)
      return Response(
        status=status.HTTP_202_ACCEPTED,
        data={'message': 'Remove like'}
      )
    data.likes.add(request.user.id)
    return Response(
        status=status.HTTP_202_ACCEPTED,
        data={'message': 'Add like'}
      )

    return Response(
      data={'hola'}
    )

  def get_serializer_class(self):
    if self.action == 'list' or self.action == 'retrieve':
      return NewsletterSerializer
    return self.serializer_class

  def get_permissions(self):
    if self.action == 'create':
        permission_classes = [IsAdminUser]
    elif self.action == 'like':
        permission_classes = [IsAuthenticated]
    else:
        permission_classes = [IsAuthenticatedOrReadOnly]
    return [permission() for permission in permission_classes]

