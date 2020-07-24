from rest_framework import serializers
from answers.models import Answer
from django.contrib.auth.models import User


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['text', 'timestamp', 'updated']


class UserSerializer(serializers.ModelSerializer):
    answers = serializers.PrimaryKeyRelatedField(many=True, queryset=Answer.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'answers']