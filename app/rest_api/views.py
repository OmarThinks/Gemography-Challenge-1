from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
import json
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
	
	#print(json.dumps(result,indent=4),flush=True)
	
	if result["success"]:
		return Response(result)
	return Response(result, 
			status=status.HTTP_422_UNPROCESSABLE_ENTITY)

@api_view(['GET'])
def github_search_repo_view_new(request):
	params = request.query_params
	serializer = GithubSearchRepoSerializer(data=request.query_params)
	serializer.is_valid(raise_exception=True)
	print(serializer.validated_data, flush =True)
	#self.perform_create(serializer)
	#headers = self.get_success_headers(serializer.data)
	"""for key in params:
		q_params[key] = params[key]
	#print(dict(q_params),flush=True)
	result = github_search_repos(**q_params)
	
	#print(json.dumps(result,indent=4),flush=True)
	
	if result["success"]:
		return Response(result)
	return Response(result, 
			status=status.HTTP_422_UNPROCESSABLE_ENTITY)"""
	return Response({"success":True})



from rest_framework import viewsets



class GithubReopsViewSet(viewsets.ViewSet):
	serializer_class = GithubReopsViewSet
	def list(self, request):
		params = request.query_params
		serializer = self.get_serializer(data=request.query_params)
		serializer.is_valid(raise_exception=True)
		print(serializer.validated_data, flush =True)
		#self.perform_create(serializer)
		#headers = self.get_success_headers(serializer.data)
		"""for key in params:
			q_params[key] = params[key]
		#print(dict(q_params),flush=True)
		result = github_search_repos(**q_params)

		#print(json.dumps(result,indent=4),flush=True)

		if result["success"]:
			return Response(result)
		return Response(result, 
				status=status.HTTP_422_UNPROCESSABLE_ENTITY)"""
		return Response({"success":True})

