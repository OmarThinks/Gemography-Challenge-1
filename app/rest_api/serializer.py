from rest_framework import serializers

from datetime import datetime

class GithubSearchRepoSerializer(serializers.Serializer):
    date = serializers.DateField()
    sort = serializers.CharField(max_length=20)
    order = serializers.CharField(max_length=20)

    def validate_date(self, value):
        """
        Validate if date is more than now
        """
        if (value > datetime.today().date()):
        	raise serializers.ValidationError(
        		"the value of date can not be in the future")
        return value

    def create(self, validated_data):
        pass
        #return Comment(**validated_data)