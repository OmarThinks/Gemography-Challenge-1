from rest_framework import serializers

from datetime import datetime


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




