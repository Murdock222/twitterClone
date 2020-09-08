from django.contrib.auth.models import AbstractUser
from django.db import models



class TwitterProfile(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    