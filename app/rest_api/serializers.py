testing=True
testing=False


from rest_framework import serializers

from datetime import datetime








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
	if testing:
		return get_formatted_data(dummy_data["data"])

	#print("queries",queries,flush=True)
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







class GithubSearchRepoSerializer(serializers.Serializer):
	date = serializers.DateField(
		format="%Y-%m-%d", input_formats=['%Y-%m-%d'])
	order = serializers.ChoiceField(
		[("desc","desc"),("asc","asc")])
	records = serializers.IntegerField(
		min_value = 1, max_value = 1000)

	def validate_date(self, date):
		"""
		Validate if date is more than now
		"""
		if (date > datetime.today().date()):
			raise serializers.ValidationError(
				"date can not be more than today")
		date = date.strftime('%Y-%m-%d')
		return date

	def get_github_urls(self):
		"""
		Returns a list of github urls that will be examined.
		Example Output:

	[
		'https://api.github.com/search/repositories?q=created:>2021-09-01&sort=stars&order=desc&per_page=100&page=1'
	]
		"""
		records = self.validated_data["records"]
		pages = int((records-1)/100) + 1
		github_urls = []
		for page in range(1,pages+1):
			toappend = ("https://api.github.com/search/"+
				"repositories?q=created:>"+
				str(self.validated_data["date"])+
				"&sort=stars&order="+
				str(self.validated_data["order"])+
				"&per_page=100&page="+
				str(page))
			github_urls.append(str(toappend))
		#print("github_urls",github_urls, flush=True)
		return github_urls

	def get_ordered_repos_response(self):
		#Returns the response to the api
		self.is_valid(raise_exception=True)
		github_request_urls = self.get_github_urls()
		response = Response({"success":True,
			"github_request_urls":github_request_urls, 
			"data": get_formatted_data_from_queries(github_request_urls,
			self.validated_data["records"])})
		return response	


