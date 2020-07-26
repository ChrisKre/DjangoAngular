from django.urls import path, include
from rest_framework import routers
from .views import RegisterViewSet

router = routers.DefaultRouter()
router.register(r'', RegisterViewSet)

urlpatterns = [
    path('', include(router.urls)),
]