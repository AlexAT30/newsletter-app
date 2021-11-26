from rest_framework.serializers import ModelSerializer

from tags.models import Tag


# default
class TagSerializer(ModelSerializer):
  class Meta:
    model = Tag
    fields = ['id', 'name', 'slug', 'created_at']

# create
class CreateTagSerializer(ModelSerializer):
  class Meta:
    model = Tag
    fields = ['name', 'slug']

