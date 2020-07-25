from rest_framework import serializers
from registers.api.serializers import RegisterSerializer
from answers.api.serializers import AnswerSerializer
from answers.models import Answer
from questions.models import Question
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'answers']


class QuestionSerializer(serializers.ModelSerializer):

    answers = AnswerSerializer(many=True)
    registers = RegisterSerializer()

    class Meta:
        model = Question
        fields = ['owner', 'text', "registers", 'timestamp', 'updated', 'answers']


