from rest_framework import serializers
from answers.models import Answer
from questions.api.serializers import QuestionSerializer


class AnswerSerializer(serializers.ModelSerializer):

    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Answer
        fields = ['id', 'text', 'questions', 'timestamp', 'updated']

