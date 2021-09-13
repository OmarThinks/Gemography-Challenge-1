from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
import json
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer

from rest_framework import viewsets
# Create your views here.

from .serializers import (GithubSearchRepoSerializer, build_queries)

from .github_search import github_search_repos


from .github_search import handle_queries




@api_view(['GET'])
def github_search_repo_view(request):
	params = request.query_params
	#print(dict(params),flush=True)
	q_params={}
	for key in params:
		q_params[key] = params[key]
	#print(dict(q_params),flush=True)
	result = github_search_repos(**q_params)
	
	#print(json.dumps(result,indent=4),flush=True)
	
	if result["success"]:
		return Response(result)
	return Response(result, 
			status=status.HTTP_422_UNPROCESSABLE_ENTITY)


def get_ordered_repos_response(serializer):
		serializer.is_valid(raise_exception=True)
		response = Response({"success":True, 
			"data": handle_queries(serializer.save(),
			serializer.validated_data["records"])})
		return response	


class GithubReopsViewSetAgain(viewsets.ViewSet):
	serializer_class = GithubSearchRepoSerializer
	renderer_classes = [JSONRenderer,BrowsableAPIRenderer]
	
	def list(self, request):
		serializer = GithubSearchRepoSerializer(
			data=request.query_params)
		return get_ordered_repos_response(serializer)

	def create(self, request):
		serializer = GithubSearchRepoSerializer(
			data=request.data)
		return get_ordered_repos_response(serializer)














