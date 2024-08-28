from django.db import models

from urlshortener.utils.generate_slug import generate_slug
from authentication.models import CustomUser


class Url(models.Model):
    url = models.CharField(max_length=255)
    clicks = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="urls")
    created_at: models.DateTimeField = models.DateTimeField(auto_now_add=True)
    updated_at: models.DateTimeField = models.DateTimeField(auto_now=True)
    slug = models.CharField(max_length=8, unique=True, default=generate_slug())

    def __unicode__(self):
        return self.name
