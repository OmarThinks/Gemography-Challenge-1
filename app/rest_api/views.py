from django.shortcuts import render

# Create your views here.

from .serializers import (GithubSearchRepoSerializer, build_queries)


@api_view(['GET'])
def github_search_repo(request):
	q_params = request.query_params
	print(q_params)
	ser = GithubSearchRepoSerializer(**q_params)
	if ser.is_valid():
		return Response(ser.save)
	return Response({"message": "Hello for today! See you tomorrow!"})