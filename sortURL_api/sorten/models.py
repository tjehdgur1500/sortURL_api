from django.db import models
from django.contrib.auth.models import User


class Sorten(models.Model):
    owner = models.ForeignKey(User, related_name='urls', on_delete=models.CASCADE)
    selfurl = models.URLField(max_length=200)
    random_int = models.BigIntegerField()
