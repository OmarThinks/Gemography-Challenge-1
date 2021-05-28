import unittest
from rest_api.serializers import build_queries

class QueriesBuilderTestCase(unittest.TestCase):
	def test_001_test(self):
		queries = build_queries(
			date = "2019-04-29", order = "asc", records=99)
		self.assertEqual(queries, [
			"https://api.github.com/search/repositories?"+
			"q=created:>{date}&sort=stars&order={order}"+
			"&per_page=100&page={page}".format(
			date = "2019-04-29", order = "asc", page = 1)])


# Make the tests conveniently executable
if __name__ == "__main__":
	unittest.main()