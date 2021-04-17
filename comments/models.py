from django.db import models
from django.utils import timezone


class BaseComment(models.Model):
    body = models.CharField(max_length=2048)
    created_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        abstract = True


class QuestionComment(BaseComment):
    question_id = models.ForeignKey('questions.Question', on_delete=models.CASCADE, db_column='question_id')


class AnswerComment(BaseComment):
    answer_id = models.ForeignKey('answers.Answer', on_delete=models.CASCADE, db_column='answer_id')