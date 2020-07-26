from django.db import models

# Create your models here.
from questions.models import Question


class Answer(models.Model):
    question = models.ForeignKey(
        Question,
        related_name='answers',
        on_delete=models.CASCADE
    )
    text = models.TextField()
    timestamp = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.text
