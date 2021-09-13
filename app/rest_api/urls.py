from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from rest_api.views import github_search_repo_view,github_search_repo_view_new,GithubReopsViewSet


router = routers.DefaultRouter()
router.register(r'repos', GithubReopsViewSet, basename ='githubrepos')


urlpatterns = [
    path('', include(router.urls)),
]


