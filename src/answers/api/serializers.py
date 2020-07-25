from rest_framework import serializers
from answers.models import Answer


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ['id', 'text', 'timestamp', 'updated']
        extra_kwargs = {'questions': {'required': True}}

