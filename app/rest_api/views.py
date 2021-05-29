from rest_framework import status
from rest_framework.response import Response

# Create your views here.

from .serializers import (GithubSearchRepoSerializer, build_queries)

import requests



def handle_queries(queries):
	# get the response from the URL
	responses = []
	for q in queries:
		responses.append(requests.get('query'))
	#result = do_something_with_response(response)
	print(responses[0])
	return responses




@api_view(['GET'])
def github_search_repo_view(request):
	q_params = request.query_params
	print(q_params)
	ser = GithubSearchRepoSerializer(**q_params)
	responses = []
	if not ser.is_valid():
		content = ser.errors
		return Response(content, 
			status=status.HTTP_422_UNPROCESSABLE_ENTITY)
	handle_queries(responses)
	return Response({"message": "Hello for today! See you tomorrow!"})


