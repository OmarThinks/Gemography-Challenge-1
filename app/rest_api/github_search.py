from .serializers import (GithubSearchRepoSerializer, build_queries)
import requests
import json


def handle_queries(queries):
	# get the response from the URL
	print("queries",queries)
	responses = []
	items = []
	for q in queries:
		response = requests.get(q)
		responses.append(response)
		res = response.json()["items"]
		for item in res:
			languages_request = requests.get(
						item["languages_url"]).json()
			item_data = {
				"url":item["html_url"],
				"name": item["name"],
				"full_name":item["full_name"],
				"language": item["language"]
				}
			items.append(item_data)
	print(json.dumps(items, indent=4, sort_keys=True))



	return responses




def github_search_repos(**kwargs):
	print(kwargs)
	ser = GithubSearchRepoSerializer(data = kwargs)
	if not ser.is_valid():
		return {"success":False, "data":ser.errors}
	return {"success":True, 
	"data": handle_queries(ser.save())}


