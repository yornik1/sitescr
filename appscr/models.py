from django.db import models

# Create your models here.


class Profile(models.Model):
    name = models.CharField(max_length=32, unique=True, null=False,
                            blank=False)
    top_count = models.PositiveIntegerField(null=True, default=None)
    videos = models.NullBooleanField(null=True, blank=True)


class Photo(models.Model):
    url = models.URLField(unique=True)
    likes = models.PositiveIntegerField(null=True)
    comments = models.PositiveIntegerField(null=True)
