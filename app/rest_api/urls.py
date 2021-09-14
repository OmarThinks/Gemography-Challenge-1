from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from rest_api.views import (GithubReopsViewSet)


router = routers.DefaultRouter()
router.register(r'github/search', GithubReopsViewSet, basename ='githubreposagain')


urlpatterns = [
    path('', include(router.urls)),
]


