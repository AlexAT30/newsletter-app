from rest_framework.serializers import ModelSerializer

from tags.models import Tag


# get (list) and not admin
class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']


# post
class CrearTagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


# retrieve and admin /
class DetalleTagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
