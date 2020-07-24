from rest_framework import serializers
from questionlist.models import QuestionList
from questions.api.serializers import QuestionSerializer


class QuestionListSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = QuestionList
        fields = ['id', 'name', 'owner', 'questions', 'type', 'timestamp', 'updated']
