from django.db import models
from django.utils import timezone
from .validators import tag_validator


class Tag(models.Model):
    name = models.CharField(max_length=255, validators=[tag_validator])

    def __str__(self):
        return self.name


class Question(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField(max_length=5000)
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title