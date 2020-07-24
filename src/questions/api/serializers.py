from rest_framework import serializers

from answers.api.serializers import AnswerSerializer
from questions.models import Question
from django.contrib.auth.models import User


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['owner', 'text', 'answers', 'timestamp', 'updated']


class UserSerializer(serializers.ModelSerializer):
    answers = serializers.PrimaryKeyRelatedField(many=True, queryset=Question.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'answers']