import unittest
from rest_api.github_search import github_search_repos


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
	def setUp(self):
		self.success_data = {
			"date":"2019-04-29", "order":"desc", "records":99}
	
	def test_001_success(self):
		search_results = github_search_repos(
			**self.success_data)
		self.assertEqual(search_results["success"],True)
		print(search_results)
		print("test_001:Sucessful search")



# Make the tests conveniently executable
if __name__ == "__main__":
	unittest.main()