from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests

# Create your views here.

from .serializers import (GithubSearchRepoSerializer, build_queries)

from .github_search import github_search_repos



def handle_queries(queries):
	# get the response from the URL
	responses = []
	for q in queries:
		responses.append(requests.get(q))
	print(responses[0])
	return responses






@api_view(['GET'])
def github_search_repo_view(request):
	params = request.query_params
	q_params={}
	for key in params:
		q_params[key] = params[key]
	result = github_search_repos(**q_params)
	if result["success"]:
		return Response(result)
	return Response(result, 
			status=status.HTTP_422_UNPROCESSABLE_ENTITY)

