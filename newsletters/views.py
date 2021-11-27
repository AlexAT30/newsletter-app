from datetime import datetime
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

  def update(self, request, pk=None):
    data = Newsletter.objects.get(id=pk)
    # Verification to the user is the person who created the newsletter or editor #
    if not data.created_by == request.user:
      if not data.editors.filter(id=request.user.id)[0] == request.user: 
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
    newsletter = Newsletter(**data)
    newsletter.id = pk
    newsletter.updated_at = datetime.now()
    newsletter.save(force_update=True)

    return Response(
      status=status.HTTP_201_CREATED,
      data={'message': 'Newsletter updated correctly'}
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

  @action(methods=['POST'], detail=True)
  def subscribe(self, request, pk=None):
    data = Newsletter.objects.get(id=pk)
    if not data.likes.all().count() >= data.target:

      missing_votes = data.target - data.likes.all().count()

      return Response(
      status=status.HTTP_202_ACCEPTED,
      data={
        'error': 'The newsletter need more votes to you can subscribe', 
        'missing_votes': missing_votes
      }
    )
    
    is_subscribed = False
    try:
      data.subscribed_users.get(id=request.user.id)
      is_subscribed = True
    except:
      pass
    if is_subscribed:
      data.subscribed_users.remove(request.user.id)
      return Response(
        status=status.HTTP_202_ACCEPTED,
        data={'message': 'Remove subscribe'}
    )
    data.subscribed_users.add(request.user.id)
    return Response(
      status=status.HTTP_202_ACCEPTED,
      data={'message': 'Add subscribe'}
    )

  @action(methods=['POST', 'DELETE'], detail=True)
  def editors(self, request, pk=None):
    data = Newsletter.objects.get(id=pk)
    if not data.created_by == request.user:
      return Response(
        status=status.HTTP_401_UNAUTHORIZED,
        data={'error': 'You don\'t have permission to do this.'}
      )
    if request.method == 'POST':
      data.editors.add(request.data['id'])
      return Response(
        data={'POST'}
      )
    if request.method == 'DELETE':
      data.editors.remove(request.data['id'])
      return Response(
        data={'DELETE'}
      )

  def get_serializer_class(self):
    if self.action == 'list' or self.action == 'retrieve':
      return NewsletterSerializer
    return self.serializer_class

  def get_permissions(self):
    if self.action == 'create' or self.action == 'update' or self.action == 'destroy':
        permission_classes = [IsAdminUser]
    elif self.action == 'like':
        permission_classes = [IsAuthenticated]
    else:
        permission_classes = [IsAuthenticatedOrReadOnly]
    return [permission() for permission in permission_classes]

