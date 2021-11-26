from django.db import models

class Tag(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=50, unique=True)
  slug = models.CharField(max_length=50, unique=True)
  created_at = models.DateField(auto_now_add=True)

  def __str__(self) -> str:
    return self.name
