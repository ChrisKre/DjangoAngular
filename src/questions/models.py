from django.contrib.auth.models import User
from django.db import models
from registers.models import Register
# Create your models here.


class Question(models.Model):
    owner = models.ForeignKey(
        User,
        related_name='questionOwner',
        on_delete=models.CASCADE
    )

    register = models.ForeignKey(
        Register,
        related_name='questions',
        on_delete=models.CASCADE
    )

    text = models.TextField()
    timestamp = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.text



