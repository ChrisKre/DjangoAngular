from rest_framework import serializers
from questions.models import Question
from registers.api.serializers import RegisterSerializer


class QuestionSerializer(serializers.ModelSerializer):
    registers = RegisterSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['owner', 'text', 'answers', 'registers']

