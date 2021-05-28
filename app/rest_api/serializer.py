from rest_framework import serializers

class GithubSearchRepoSerializer(serializers.Serializer):
    date = serializers.DateField()
    sort = serializers.CharField(max_length=20)
    order = serializers.CharField(max_length=20)
		