from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Answer(models.Model):
    #owner = models.ForeignKey(User, related_name='answerOwner', on_delete=models.CASCADE)
    text = models.TextField()
    timestamp = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.text