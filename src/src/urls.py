"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework.documentation import include_docs_urls
from django.conf.urls import include, url
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    path('admin/', admin.site.urls),
    path(r'api/', include_docs_urls(title='API Overview')),
    path(r'api/answers/', include('answers.api.urls'), name='api-answers'),
    path(r'api/questions/', include('questions.api.urls'), name='api-questions'),
    path(r'api/registers/', include('registers.api.urls'), name='api-registers'),
    #path(r'api/questionlist/', include('questionlist.api.urls'), name='api-questionlist')
]
