from django.urls import path, include
from rest_framework import routers
from .views import AnswerViewSet

router = routers.DefaultRouter()
router.register(r'answers', AnswerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]