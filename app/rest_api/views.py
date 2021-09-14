from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
import json
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer

from rest_framework import viewsets
# Create your views here.

from .serializers import (GithubSearchRepoSerializer)

#from .github_search import (github_search_repos,get_ordered_repos_response)


#from .github_search import get_formatted_data


class GithubReopsViewSet(viewsets.ViewSet):
	serializer_class = GithubSearchRepoSerializer
	renderer_classes = [JSONRenderer,BrowsableAPIRenderer]
	
	def list(self, request):
		serializer = GithubSearchRepoSerializer(
			data=request.query_params)
		return serializer.get_ordered_repos_response()

	def create(self, request):
		serializer = GithubSearchRepoSerializer(
			data=request.data)
		return serializer.get_ordered_repos_response()














