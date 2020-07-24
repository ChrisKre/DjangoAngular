from django.db import models
from django.contrib.auth.models import User
from questions.models import Question
from django.utils.translation import gettext_lazy as _
# Create your models here.


class QuestionList(models.Model):

    class QuestionListType(models.TextChoices):
        LANGUAGE = 'LAN', _('Language')
        SOFTWARE = 'SFW', _('Software')
        KNOWLEDGE = 'KLG', _('Knowledge')

    owner = models.ForeignKey(
        User,
        related_name='questionListOwner',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=50)
    questions = models.ManyToManyField(Question)
    timestamp = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    type = models.CharField(
        max_length=3,
        choices=QuestionListType.choices,
        default=QuestionListType.LANGUAGE
    )

    def __str__(self):
        return self.name
