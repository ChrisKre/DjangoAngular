from django.urls import path, include
from rest_framework import routers
from .views import QuestionViewSet

router = routers.DefaultRouter()
router.register(r'', QuestionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]