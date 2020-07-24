from questionlist.api.serializers import QuestionListSerializer
from questionlist.models import QuestionList
from rest_framework import viewsets


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = QuestionList.objects.all()
    serializer_class = QuestionListSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
