from .serializers import (GithubSearchRepoSerializer, build_queries)
import requests
import json

from rest_api.dummy_data import dummy_data

def handle_data(data):
	#print(len(data))
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
	handled_data = []
	for l_name in sorted_languages_names:
		handled_data.append(
			formatted_data[l_name])
	return handled_data





def handle_queries(queries,records):
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
	return handle_data(items[0:records])


def github_search_repos(**kwargs):
	#print(kwargs)
	ser = GithubSearchRepoSerializer(data = kwargs)
	if not ser.is_valid():
		return {"success":False, "data":ser.errors}
	return {"success":True, 
	"data": handle_queries(ser.save(),
		ser.validated_data["records"])}


