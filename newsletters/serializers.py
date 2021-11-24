from rest_framework.serializers import ModelSerializer

from newsletters.models import Newsletter


# get (list) and not admin
class NewsletterSerializer(ModelSerializer):
    class Meta:
        model = Newsletter
        fields = ['name', 'img']


# post
class CrearNewsletterSerializer(ModelSerializer):
    class Meta:
        model = Newsletter
        fields = '__all__'


# retrieve and admin /
class DetalleNewsletterSerializer(ModelSerializer):
    class Meta:
        model = Newsletter
        fields = '__all__'
