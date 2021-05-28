import unittest
from rest_api.serializers import (
	build_queries, GithubSearchRepoSerializer)


"""
Here we will test the 
"""

"""
To run the tests

pytest
pytest -rP
pytest -rP --junitxml=test-reports/junit.xml --html=test-reports/pytest_report.html --self-contained-html
"""



class GithubSearchRepoSerializerTestCase(unittest.TestCase):
	def test_001_failure(self):
		ser = GithubSearchRepoSerializer(data={
			"date":"abc", "order":123, "records":100000000})
		#ser.validate()
		print(ser.is_valid())

		print("test_001:asc one page")

	def test_002(self):
		queries = build_queries(
			date = "2019-04-29", order = "decs", records=100)
		self.assertEqual(queries, [
			"https://api.github.com/search/repositories?"+
			"q=created:>{date}&sort=stars&order={order}"+
			"&per_page=100&page={page}".format(
			date = "2019-04-29", order = "decs", page = 1)])
		print("test_001:decs one page on the edge")

	def test_003(self):
		queries = build_queries(
			date = "2019-04-29", order = "decs", records=101)
		self.assertEqual(queries, [
			"https://api.github.com/search/repositories?"+
			"q=created:>{date}&sort=stars&order={order}"+
			"&per_page=100&page={page}".format(
			date = "2019-04-29", order = "decs", page = 1),
			"https://api.github.com/search/repositories?"+
			"q=created:>{date}&sort=stars&order={order}"+
			"&per_page=100&page={page}".format(
			date = "2019-04-29", order = "decs", page = 2),
			])
		print("test_001:decs 2 pages")


# Make the tests conveniently executable
if __name__ == "__main__":
	unittest.main()