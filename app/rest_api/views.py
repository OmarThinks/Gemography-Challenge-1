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






"""

from pprint import pp
class CustomBrowsableAPIRenderer(BrowsableAPIRenderer):	
	def get_context(
		self, data, accepted_media_type, renderer_context):
		context = BrowsableAPIRenderer.get_context(
			self, data, accepted_media_type, renderer_context)
		
		try:
			serializer = data.serializer
			print(serializer)
			form_renderer = self.form_renderer_class()
			form = form_renderer.render(
				serializer.data,
				self.accepted_media_type,
				{'style': {'template_pack': 'rest_framework/horizontal'}}
			)
			context["put_form"] = form
			print(form)
		except Exception as e:
			pass
		return context



"""















class GithubReopsViewSetAgain(viewsets.ViewSet):
	serializer_class = GithubSearchRepoSerializer
	renderer_classes = [
	JSONRenderer,BrowsableAPIRenderer]
	
	def list(self, request):
		serialzer = serializer = GithubSearchRepoSerializer(
			data=request.query_params)
		if serializer.is_valid(raise_exception=True):
			response = Response(serializer.validated_data)
		else:
			response = Response(serializer.errors)
		return response

	def create(self, request):
		serialzer = serializer = GithubSearchRepoSerializer(
			data=request.data)
		if serializer.is_valid(raise_exception=True):
			response = Response(serializer.validated_data)
		else:
			response = Response(serializer.errors)
		return response













