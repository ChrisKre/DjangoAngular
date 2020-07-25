from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from questions.models import Question
# Create your models here.


class Register(models.Model):

    class RegisterType(models.TextChoices):
        LANGUAGE = 'LAN', _('Language')
        SOFTWARE = 'SFW', _('Software')
        KNOWLEDGE = 'KLG', _('Knowledge')

    owner = models.ForeignKey(
        User,
        related_name='questionRegisterOwners',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=50)
    questions = models.ManyToManyField(Question, through='RegisterQuestion')
    timestamp = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    type = models.CharField(
        max_length=3,
        choices=RegisterType.choices,
        default=RegisterType.LANGUAGE
    )

    def __str__(self):
        return self.name


class RegisterQuestion(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    register = models.ForeignKey(Register, on_delete=models.CASCADE)

    def __str__(self):
        return self.register.name