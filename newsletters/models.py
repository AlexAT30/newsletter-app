from django.db import models

from tags.models import Tag

class Newsletter(models.Model):
  name = models.CharField(max_length=100, default='dummy text')
  description = models.CharField(max_length=400, default='dummy description')
  img = models.CharField(max_length=100, default='image_dummmy_url')
  # target  <- no se que tipo de dato deba usarse
  # frecuency
  # created_by = models.ForeignKey(User)
  tags = models.ManyToManyField(Tag, related_name='tags')
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now_add=True)

  def __str__(self) -> str:
    return self.name
