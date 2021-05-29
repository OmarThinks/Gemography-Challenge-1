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




def github_search_repos(**kwargs):
	print(q_params)
	ser = GithubSearchRepoSerializer(data = **kwargs)
	responses = []
	if not ser.is_valid():
		return {"success":False, "data":ser.errors}
	return {"success":True, "data":handle_queries(responses)}


