from django.db import models
from django.utils import timezone


class Answer(models.Model):
    question_id = models.ForeignKey('questions.Question', on_delete=models.CASCADE, db_column='question_id')
    body = models.TextField(max_length=5000)
    created_at = models.DateTimeField(default=timezone.now)