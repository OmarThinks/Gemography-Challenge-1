from .serializers import (GithubSearchRepoSerializer)
import requests
import json

from rest_api.dummy_data import dummy_data
from rest_framework.response import Response


from pprint import pp

"""
Function:
This gets the raw data of the github request,
format it to the right way to be returned by the API.


Input Example:

[{'url': 'https://github.com/ErickWendel/semana-javascript-expert05',
  'name': 'semana-javascript-expert05',
  'full_name': 'ErickWendel/semana-javascript-expert05',
  'language': 'JavaScript'},
 {'url': 'https://github.com/StarRocks/starrocks',
  'name': 'starrocks',
  'full_name': 'StarRocks/starrocks',
  'language': 'C++'},
...
]


Output Example:

[{'repos': [{'url': 'https://github.com/ErickWendel/semana-javascript-expert05',
             'name': 'semana-javascript-expert05',
             'full_name': 'ErickWendel/semana-javascript-expert05',
             'language': 'JavaScript'},
            {'url': 'https://github.com/EtherDream/web2img',
             'name': 'web2img',
             'full_name': 'EtherDream/web2img',
             'language': 'JavaScript'},
             ...
             ],
  'length': 7,
  'language': 'JavaScript'},

 {'repos': [...],
  'length': 7,
  'language': 'Python'},

]

 

"""
def get_formatted_data(data):
	#print(len(data))
	#pp(data)
	formatted_data = dict()
	for repo in data:
		lang = str(repo["language"])
		if lang == "None":
			continue
		if formatted_data.get(lang) == None:
			formatted_data[lang] = {
			"repos":[],
			"length":0,
			"language": lang
			}
		formatted_data[lang]["repos"].append(repo)
		formatted_data[lang]["length"] =len(
			formatted_data[lang]["repos"])
	#print(formatted_data.items())
	sorted_languages_names = sorted(formatted_data, 
		key=lambda item: formatted_data[item]["length"],
		reverse=True)
	final_formatted_data = []
	for l_name in sorted_languages_names:
		final_formatted_data.append(
			formatted_data[l_name])
	#pp(formatted_data)
	#pp(final_formatted_data)
	return final_formatted_data






"""
Function:
Get the formatted data for list of queries


Input:
[
	'https://api.github.com/search/repositories?q=created:>2021-09-01&sort=stars&order=desc&per_page=100&page=1'
]



Output Example:

[{'repos': [{'url': 'https://github.com/ErickWendel/semana-javascript-expert05',
             'name': 'semana-javascript-expert05',
             'full_name': 'ErickWendel/semana-javascript-expert05',
             'language': 'JavaScript'},
            {'url': 'https://github.com/EtherDream/web2img',
             'name': 'web2img',
             'full_name': 'EtherDream/web2img',
             'language': 'JavaScript'},
             ...
             ],
  'length': 7,
  'language': 'JavaScript'},

 {'repos': [...],
  'length': 7,
  'language': 'Python'},

]


"""






def get_formatted_data_from_queries(queries,records):
	print("queries",queries,flush=True)
	#print("records",records,flush=True)
	#print("records",type(records),flush=True)
	# get the response from the URL
	#print("queries",queries)
	items = []
	#requests.get(q).json()["items"]
	for q in queries:
		requested_items = requests.get(q).json()["items"]
		for item in requested_items:
			item_data = {
				"url":item["html_url"],
				"name": item["name"],
				"full_name":item["full_name"],
				"language": item["language"]
				}
			items.append(item_data)
	return get_formatted_data(items[0:records])



def get_ordered_repos_response(serializer):
		serializer.is_valid(raise_exception=True)
		github_request_urls = serializer.get_github_urls()
		response = Response({"success":True,
			"github_request_urls":github_request_urls, 
			"data": get_formatted_data_from_queries(github_request_urls,
			serializer.validated_data["records"])})
		return response	








def github_search_repos(**kwargs):
	#print(kwargs)
	ser = GithubSearchRepoSerializer(data = kwargs)
	if not ser.is_valid():
		return {"success":False, "data":ser.errors}
	return {"success":True, 
	"data": get_formatted_data_from_queries(ser.get_github_urls(),
		ser.validated_data["records"])}


