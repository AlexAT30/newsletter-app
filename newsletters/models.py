from django.db import models
from users.models import User
from tags.models import Tag

class Newsletter(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=100, default='dummy text')
  description = models.CharField(max_length=400, default='dummy description')
  image_url = models.CharField(max_length=100, default='image_dummmy_url')
  target = models.IntegerField(default=10)
  likes = models.ManyToManyField(User, related_name='likes')
  # frecuency
  created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
  tags = models.ManyToManyField(Tag, related_name='tags')
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now_add=True)

  def __str__(self) -> str:
    return self.name
