from django.contrib.auth.models import User
from django.db import models
from answers.models import Answer
# Create your models here.


class Question(models.Model):
    owner = models.ForeignKey(
        User,
        related_name='questionOwner',
        on_delete=models.CASCADE
    )
    answers = models.ManyToManyField(Answer, related_name='questions')
    text = models.TextField()
    timestamp = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.text



