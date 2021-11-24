from rest_framework.viewsets import ModelViewSet

from newsletters.models import Newsletter
from newsletters.serializers import NewsletterSerializer, CrearNewsletterSerializer, DetalleNewsletterSerializer


class NewslettersViewSet(ModelViewSet):
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer

    def get_serializer_class(self):
        if self.action == 'list' and not self.request.user.is_staff:
            return NewsletterSerializer

        if self.request.method == 'POST':
            return CrearNewsletterSerializer

        if self.action == 'retrieve' and self.request.user.is_staff:
            return DetalleNewsletterSerializer

        return NewsletterSerializer
