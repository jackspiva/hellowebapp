from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Create your models here.
class Worksheet(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    user = models.OneToOneField(User, blank=True, null=True)

class Post(models.Model):
    author = models.TextField()
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    worksheet = models.ForeignKey(to=Worksheet, related_name="entries", blank=True, null=True)
