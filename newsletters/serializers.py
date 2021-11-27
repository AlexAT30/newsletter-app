from rest_framework.serializers import ModelSerializer
from newsletters.models import Newsletter
from tags.serializers import TagSerializer
from users.serializers import MinimalUserSerializer, UserSerializer


# Default
class NewsletterSerializer(ModelSerializer):
  tags = TagSerializer(many=True)
  created_by = MinimalUserSerializer()
  likes = MinimalUserSerializer(many=True)
  subscribed_users = MinimalUserSerializer(many=True)
  editors = MinimalUserSerializer(many=True)
  class Meta:
    model = Newsletter
    fields = ['id', 'name', 'image_url', 'description', 'editors', 'target', 'likes', 'subscribed_users', 'created_by', 'tags', 'created_at', 'updated_at']

# Create
class CreateNewsletterSerializer(ModelSerializer):
  class Meta:
    model = Newsletter
    fields = ['name', 'image_url', 'description', 'target', 'created_by']

# ToUsers
class ToUsersNewsletterSerializer(ModelSerializer):
  tags = TagSerializer(many=True)
  created_by = MinimalUserSerializer()
  editors = MinimalUserSerializer(many=True)
  class Meta:
    model = Newsletter
    fields = ['id', 'name', 'image_url', 'description', 'editors', 'created_by', 'tags']