from rest_framework.serializers import ModelSerializer
from .models import Explanation, Document, Company_cars_request

class ExplanationSerializer(ModelSerializer):
    class Meta:
        model = Explanation
        fields = "__all__"

class DocumentSerializer(ModelSerializer):
    class Meta:
        model = Document
        fields = "__all__"

class Company_cars_requestSerializer(ModelSerializer):
    class Meta:
        model = Company_cars_request
        fields = "__all__"