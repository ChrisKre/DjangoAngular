from registers.api.serializers import RegisterSerializer
from registers.models import Register
from rest_framework import viewsets


class RegisterViewSet(viewsets.ModelViewSet):
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
