from rest_framework import serializers

class Work_permitSerializer(serializers.Serializer):

     pk = serializers.IntegerField()
     name = serializers.CharField(required=True)
     created_at = serializers.DateTimeField()