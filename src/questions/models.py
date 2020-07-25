from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from answers.models import Answer


class Question(models.Model):
    owner = models.ForeignKey(
        User,
        related_name='questionOwner',
        on_delete=models.CASCADE
    )
    answers = models.ManyToManyField(Answer, through='QuestionAnswer')
    text = models.TextField()
    timestamp = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.text


class QuestionAnswer(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.question.text




