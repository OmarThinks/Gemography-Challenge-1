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
		print("test_002:Wrong date 1")

	def test_003_date_failure_2(self):
		wrong_date_data = dict(self.success_data)
		wrong_date_data["date"] = "2019/04/29"
		ser = GithubSearchRepoSerializer(data=wrong_date_data)
		self.assertEqual(ser.is_valid(),False)
		print("test_003:Wrong date 2")

	def test_004_order_failure(self):
		wrong_order_data = dict(self.success_data)
		wrong_order_data["order"] = "aaaaaaaa"
		ser = GithubSearchRepoSerializer(data=wrong_order_data)
		self.assertEqual(ser.is_valid(),False)
		print("test_004:Wrong Order")

	def test_005_records_failure(self):
		wrong_records_data = dict(self.success_data)
		wrong_records_data["order"] = 10000000000 
		#Too amny records
		ser = GithubSearchRepoSerializer(data=wrong_records_data)
		self.assertEqual(ser.is_valid(),False)
		print("test_005:Wrong Records")


	def test_006_queries(self):
		ser = GithubSearchRepoSerializer(data=self.success_data)
		self.assertEqual(ser.is_valid(),True)
		queries = ser.save()
		#print(queries)
		self.assertEqual(queries,[
			'https://api.github.com/search/'+
			'repositories?q=created:>2019-04-29&sort='+
			'stars&order=asc&per_page=100&page=1'])
		print("test_006:Serializer building Queries")



# Make the tests conveniently executable
if __name__ == "__main__":
	unittest.main()