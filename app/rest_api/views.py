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




from rest_framework.renderers import (
	BrowsableAPIRenderer, TemplateHTMLRenderer, JSONRenderer)
from rest_framework.decorators import action, renderer_classes


from rest_framework.renderers import HTMLFormRenderer


class GithubReopsViewSet(viewsets.ViewSet):
	serializer_class = GithubSearchRepoSerializer
	def list(self, request):
		params = request.query_params
		serializer = GithubSearchRepoSerializer(data=request.query_params)
		serializer.is_valid(raise_exception=False)
		#print(serializer.validated_data, flush =True)
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
		#print("view",view)
		data = serializer.data
		#print("data",data)
		renderer_context["post_form"] = BrowsableAPIRenderer.get_rendered_html_form(
			self = self.get_renderers()[1], data = data, 
			view=view, method='POST', request = request)
		#renderer_context["post_form"] = serializer
		renderer_context["display_edit_forms"]=True
		#print(renderer_context["post_form"], flush=True)
		#print("type", type(renderer_context["post_form"]), flush=True)
		response.renderer_context = renderer_context
		

		print("type",type(response.renderer_context))
		print("renderer_context",response.renderer_context)
		
		renderer = HTMLFormRenderer()
		renderer.render(serializer)
		print("renderer",renderer.__dict__)
		post_form=HTMLFormRenderer.render(self = HTMLFormRenderer(),
			data=serializer)

		print("post_form",post_form)
		
		return response

		@action(detail=True, methods=['get'])
		def scratch(self, request):
			return Response({"success":True})


	

from pprint import pp
class CustomBrowsableAPIRenderer(BrowsableAPIRenderer):	
	def get_context(
		self, data, accepted_media_type, renderer_context):
		context = BrowsableAPIRenderer.get_context(
			self, data, accepted_media_type, renderer_context)
		context["display_edit_forms "]=True
		context["Hey"]="Wassup"
		view = renderer_context['view']
		request = renderer_context['request']
		context["post_form"]=self.get_rendered_html_form(
			data, view, 'POST', request)
		context["raw_data_post_form"] = self.get_raw_data_form(
			data, view, 'POST', request)
		
		print("self","\n\n")
		pp(self.__dict__)
		
		print("data","\n\n")
		pp(data.__dict__)
		
		print("view","\n\n")
		pp(view.__dict__)
		
		print("request","\n\n")
		pp(request.__dict__)
		pp(context)
		
		serializer = data.serializer
		print(serializer)
		form_renderer = self.form_renderer_class()
		form = form_renderer.render(
			serializer.data,
			self.accepted_media_type,
			{'style': {'template_pack': 'rest_framework/horizontal'}}
		)

		print(form)
		print(form.__dict__)

		context["put_form"] = form



		return context













from django.shortcuts import render

@api_view(['GET'])
@renderer_classes([
	JSONRenderer,CustomBrowsableAPIRenderer])
def github_search_repo_view_mod(request):
	serializer = GithubSearchRepoSerializer(
		data=request.query_params)
	if serializer.is_valid(raise_exception=False):
		response = Response(serializer.validated_data)
		#print("serialzer is valid")
	else:
		response = Response(serializer.errors)		
		#print("serialzer is not valid")
	#print(response.renderer_context)
	"""response.renderer_context={"display_edit_forms ":True,
	"post_form":True,"content":"adkjaksj","urlize":"adkjaksj",
	"raw_data_post_form ":"sfljsldkfjs",
	"abc":"ad;kjd"}
	response.context = {"display_edit_forms ":True,
	"post_form":True,"content":"adkjaksj","urlize":"adkjaksj",
	"raw_data_post_form ":"sfljsldkfjs",
	"abc":"ad;kjd"}"""
	#return response
	print(response.__dict__)
	return render(request, "backend_base.html")





@api_view(['GET'])
@renderer_classes([
	JSONRenderer, CustomBrowsableAPIRenderer])
def github_search_repo_view_compare(request):
	serialzer = serializer = GithubSearchRepoSerializer(
		data=request.query_params)
	if serializer.is_valid(raise_exception=False):
		response = Response(serializer.validated_data)
		#print("serialzer is valid")
	else:
		response = Response(serializer.errors)
	
	response.context_data = {"Hey":"Wassup"}
	print(response.__dict__)

	rendered = response.render()


	print(rendered)

	return response














class GithubReopsViewSetAgain(viewsets.ViewSet):
	serializer_class = GithubSearchRepoSerializer
	renderer_classes = [
	JSONRenderer,CustomBrowsableAPIRenderer]
	
	def list(self, request):
		serialzer = serializer = GithubSearchRepoSerializer(
			data=request.query_params)
		if serializer.is_valid(raise_exception=True):
			response = Response(serializer.validated_data)
		else:
			response = Response(serializer.errors)
		
		return response











