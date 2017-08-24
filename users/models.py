from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    user = models.OneToOneField(User)
