from rest_framework import serializers
from answers.api.serializers import AnswerSerializer
from questions.models import Question


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['text', 'register', 'answers']

