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
	def setUp(self):
		self.success_data = {
			"date":"2019-04-29", "order":"asc", "records":99}
	
	def test_001_success(self):
		ser = GithubSearchRepoSerializer(data=self.success_data)
		self.assertEqual(ser.is_valid(),True)
		#print(dict(ser.validated_data))
		self.assertEqual(dict(ser.validated_data),
			self.success_data)
		print("test_001:Sucessful Serialization")
	
	def test_002_date_failure_1(self):
		wrong_date_data = dict(self.success_data)
		wrong_date_data["date"] = 123
		ser = GithubSearchRepoSerializer(data=wrong_date_data)
		self.assertEqual(ser.is_valid(),False)
		print("test_001:Wrong date 1")

	def test_002_date_failure_2(self):
		wrong_date_data = dict(self.success_data)
		wrong_date_data["date"] = "2019/04/29"
		ser = GithubSearchRepoSerializer(data=wrong_date_data)
		self.assertEqual(ser.is_valid(),False)
		print("test_001:Wrong date 2")

	def test_003_order_failure(self):
		wrong_order_data = dict(self.success_data)
		wrong_order_data["order"] = "aaaaaaaa"
		ser = GithubSearchRepoSerializer(data=wrong_order_data)
		self.assertEqual(ser.is_valid(),False)
		print("test_001:Wrong Order")

	def test_004_records_failure(self):
		wrong_records_data = dict(self.success_data)
		wrong_records_data["order"] = 10000000000 
		#Too amny records
		ser = GithubSearchRepoSerializer(data=wrong_records_data)
		self.assertEqual(ser.is_valid(),False)
		print("test_001:Wrong Records")

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