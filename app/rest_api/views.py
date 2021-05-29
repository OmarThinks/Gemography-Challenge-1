from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests

# Create your views here.

from .serializers import (GithubSearchRepoSerializer, build_queries)




def handle_queries(queries):
	# get the response from the URL
	responses = []
	for q in queries:
		responses.append(requests.get(q))
	print(responses[0])
	return responses






@api_view(['GET'])
def github_search_repo_view(request):
	q_params = request.query_params
	print(q_params)
	ser = GithubSearchRepoSerializer(data = q_params)
	responses = []
	if not ser.is_valid():
		errors = ser.errors
		return Response({"errors":errors, "success":False}, 
			status=status.HTTP_422_UNPROCESSABLE_ENTITY)
	handle_queries(responses)
	return Response({"message": "Hello for today! See you tomorrow!"})


