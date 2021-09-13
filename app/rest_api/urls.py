from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from rest_api.views import (
	github_search_repo_view,
	GithubReopsViewSetAgain)


router = routers.DefaultRouter()
router.register(r'again', GithubReopsViewSetAgain, basename ='githubreposagain')


urlpatterns = [
    path('', include(router.urls)),
]


