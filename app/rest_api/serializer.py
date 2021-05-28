from rest_framework import serializers

from datetime import datetime

def build_queries(date, order, records):
	pages = int(records/100) + 1
	queries = []
	for page in xrange(1,pages+1):
		queries.append(
			"https://api.github.com/search/repositories?"+
			"q=created:>{date}&sort=stars&order={order}".
			"&per_page=100&page={page}".format(
			date = date, order = order, page = page)	
			)
	return queries





class GithubSearchRepoSerializer(serializers.Serializer):
    date = serializers.DateField(
        format="%d-%m-%Y", input_formats=['%d-%m-%Y'])
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
        return date

    def create(self, validated_data):
        return build_queries(**validated_data)
