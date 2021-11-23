from django.db import models

class Tag(models.Model):
  name = models.CharField(max_length=50, default='dummyTag')
  # slug
  created_at = models.DateField(auto_now_add=True)

  def __str__(self) -> str:
    return self.name
