import unittest
from rest_api.serializers import GithubSearchRepoSerializer
import json

"""
Here we will test the rest_api/github_search.py
"""

"""
To run the tests

pytest
pytest -rP
pytest -rP --junitxml=test-reports/junit.xml --html=test-reports/pytest_report.html --self-contained-html
"""



class GithubSearchRepoSerializerTestCase(unittest.TestCase):	
	def test_001_success(self):
		serializer = GithubSearchRepoSerializer(data ={
			"date" : "2019-04-29", 
			"order" : "desc", 
			"records":99
			})
		serializer.is_valid()
		search_results = serializer.get_ordered_repos_response().data


		#print(search_results)
		#print(json.dumps(search_results, indent=4, sort_keys=True))
		
		self.assertEqual(search_results["success"],True)
		data = search_results["data"]
		for language in data:
			self.assertEqual(type(language["language"]),str)
			self.assertEqual(language["length"]>=1,True)
			for repo in language["repos"]:
				self.assertEqual(type(repo["url"]),str)
				self.assertEqual(type(repo["name"]),str)
				self.assertEqual(type(repo["full_name"]),str)
				self.assertEqual(repo["language"],
					language["language"])

		print("test_001:Sucessful search")



# Make the tests conveniently executable
if __name__ == "__main__":
	unittest.main()