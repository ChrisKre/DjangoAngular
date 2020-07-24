from answers.api.serializers import AnswerSerializer
from answers.models import Answer
from rest_framework import viewsets


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    def perform_create(self, serializer):
        serializer.save()
