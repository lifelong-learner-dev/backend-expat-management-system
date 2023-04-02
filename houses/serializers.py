from rest_framework.serializers import ModelSerializer
from .models import Clause, Explanation, Regulation, House

class ClauseSerializer(ModelSerializer):
    class Meta:
        model = Clause
        fields = "__all__"

class ExplanationSerializer(ModelSerializer):
    class Meta:
        model = Explanation
        fields = "__all__"

class RegulationSerializer(ModelSerializer):
    class Meta:
        model = Regulation
        fields = "__all__"

class HouseSerializer(ModelSerializer):
    class Meta:
        model = House
        fields = "__all__"