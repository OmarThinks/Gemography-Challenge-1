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




from rest_framework.renderers import BrowsableAPIRenderer

class GithubReopsViewSet(viewsets.ViewSet):
	serializer_class = GithubSearchRepoSerializer
	def list(self, request):
		params = request.query_params
		serializer = GithubSearchRepoSerializer(data=request.query_params)
		serializer.is_valid(raise_exception=False)
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

		#print(serializer.__dir__(), flush=True)
		#print(serializer.data.copy(), flush=True)
		response = Response({"success":True})
		
		renderer_context = self.get_renderer_context()
		view = renderer_context['view']
		print("view",view)
		data = serializer.data.copy()
		print("data",data)
		renderer_context["put_form"] = (
			BrowsableAPIRenderer.get_rendered_html_form(
			self = self.get_renderers()[1], data = data, 
			view=view, method='PUT', request = request))
		print(renderer_context["put_form"], flush=True)
		print("type", type(renderer_context["put_form"]), flush=True)
		response.renderer_context = renderer_context
		#print(type(renderer_context))
		#print((renderer_context))
		return response

