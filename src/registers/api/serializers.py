from rest_framework import serializers
from questions.api.serializers import QuestionSerializer
from registers.models import Register


class RegisterSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Register
        fields = ['owner', 'name', 'questions', 'type']

