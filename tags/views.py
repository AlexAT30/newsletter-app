from rest_framework.viewsets import ModelViewSet

from tags.models import Tag
from tags.serializers import TagSerializer, CrearTagSerializer, DetalleTagSerializer


class NewslettersViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    def get_serializer_class(self):
        if self.action == 'list' and not self.request.user.is_staff:
            return TagSerializer

        if self.request.method == 'POST':
            return CrearTagSerializer

        if self.action == 'retrieve' and self.request.user.is_staff:
            return DetalleTagSerializer

        return TagSerializer
