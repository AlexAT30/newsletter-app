from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
  profile_image_url = models.CharField(max_length=200, null=True)
  birth_date = models.DateField(null=True)




