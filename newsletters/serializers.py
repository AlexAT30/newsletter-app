from rest_framework.serializers import ModelSerializer
from newsletters.models import Newsletter
from tags.serializers import TagSerializer
from users.serializers import MinimalUserSerializer, UserSerializer


# Default
class NewsletterSerializer(ModelSerializer):
  tags = TagSerializer(many=True)
  created_by = MinimalUserSerializer()
  likes = MinimalUserSerializer(many=True)
  class Meta:
    model = Newsletter
    fields = ['id', 'name', 'image_url', 'description', 'target', 'likes', 'created_by', 'tags']

# Create
class CreateNewsletterSerializer(ModelSerializer):
  class Meta:
    model = Newsletter
    fields = ['name', 'image_url', 'description', 'target', 'created_by', 'likes']
