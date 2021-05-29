from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests

# Create your views here.

from .serializers import (GithubSearchRepoSerializer, build_queries)

from .github_search import github_search_repos




@api_view(['GET'])
def github_search_repo_view(request):
	params = request.query_params
	#print(dict(params),flush=True)
	q_params={}
	for key in params:
		q_params[key] = params[key]
	#print(dict(q_params),flush=True)
	result = github_search_repos(**q_params)
	
	if result["success"]:
		return Response(result)
	return Response(result, 
			status=status.HTTP_422_UNPROCESSABLE_ENTITY)
