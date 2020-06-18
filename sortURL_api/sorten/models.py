from django.db import models
from django.contrib.auth.models import User

class Sorten(models.Model):
    owner = models.ForeignKey(User, related_name='urls', on_delete=models.CASCADE, null=True)
    selfurl = models.URLField(max_length=200)
    shorturl = models.CharField(max_length=200)
    count = models.IntegerField(default=0)