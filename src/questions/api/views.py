from questions.api.serializers import QuestionSerializer
from questions.models import Question
from rest_framework import viewsets


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
