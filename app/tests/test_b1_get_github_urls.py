import unittest
from rest_api.serializers import GithubSearchRepoSerializer


"""
Here we will test the queries builder
"""

"""
To run the tests

pytest
pytest -rP
pytest -rP --junitxml=test-reports/junit.xml --html=test-reports/pytest_report.html --self-contained-html
"""



class QueriesBuilderTestCase(unittest.TestCase):

	def test_000(self):
		self.assertEqual(
			"{date_format} {order_format} {page}".format(
			date_format="123", order_format="456", page=1),
			"123 456 1")
		self.assertEqual("https://api.github.com/search/repositories?q=created:>{date_format}&sort=stars&order={order_format}&per_page=100&page={page}".format(
			date_format = "123", order_format = "456", page = 1),
			"https://api.github.com/search/repositories?q=created:>123&sort=stars&order=456&per_page=100&page=1"
			)
		
		mysrt = "https://api.github.com/search/repositories?"+"q=created:>{date_format}&sort=stars&order={order_format}"+"&per_page=100&page={page}"
		
		mysrt.format(date_format = "123", order_format = "456", page = 1)
		#print(mysrt)
		print("test_000:testing string formatting")


	def test_001(self):
		serializer = GithubSearchRepoSerializer(data ={
			"date" : "2019-04-29", 
			"order" : "asc", 
			"records":99
			})
		serializer.is_valid()
		queries = serializer.get_github_urls()
		self.assertEqual(queries, [
			"https://api.github.com/search/repositories?"+
			"q=created:>2019-04-29&sort=stars&order=asc"+
			"&per_page=100&page=1"])
		print("test_001:asc one page")

	def test_002(self):
		serializer = GithubSearchRepoSerializer(data ={
			"date" : "2019-04-29", 
			"order" : "desc", 
			"records":100
			})
		serializer.is_valid()
		queries = serializer.get_github_urls()

		#print(queries)
		self.assertEqual(queries, [
			"https://api.github.com/search/repositories?"+
			"q=created:>2019-04-29&sort=stars&order=desc"+
			"&per_page=100&page=1"])
		print("test_002:decs one page on the edge")

	def test_003(self):
		serializer = GithubSearchRepoSerializer(data ={
			"date" : "2019-04-29", 
			"order" : "desc", 
			"records":101
			})
		serializer.is_valid()
		queries = serializer.get_github_urls()

		self.assertEqual(queries, [
			"https://api.github.com/search/repositories?"+
			"q=created:>2019-04-29&sort=stars&order=desc"+
			"&per_page=100&page=1",
			"https://api.github.com/search/repositories?"+
			"q=created:>2019-04-29&sort=stars&order=desc"+
			"&per_page=100&page=2"
			])
		print("test_003:decs 2 pages")


# Make the tests conveniently executable
if __name__ == "__main__":
	unittest.main()