from rest_framework.serializers import ModelSerializer
from .models import Explanation, Document, Visit_place, Additional_information

class ExplanationSerializer(ModelSerializer):
    class Meta:
        model = Explanation
        fields = "__all__"

class DocumentSerializer(ModelSerializer):
    class Meta:
        model = Document
        fields = "__all__"

class Visit_placeSerializer(ModelSerializer):
    class Meta:
        model = Visit_place
        fields = "__all__"

class Additional_informationListSerializer(ModelSerializer):
    class Meta:
        model = Additional_information
        fields = ("pk", "name", "subject", "created_at", "updated_at",)