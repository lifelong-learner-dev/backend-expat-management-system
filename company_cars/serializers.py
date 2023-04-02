from rest_framework.serializers import ModelSerializer
from .models import Explanation, Document, Company_car

class ExplanationSerializer(ModelSerializer):
    class Meta:
        model = Explanation
        fields = "__all__"

class DocumentSerializer(ModelSerializer):
    class Meta:
        model = Document
        fields = "__all__"

class Company_carSerializer(ModelSerializer):
    class Meta:
        model = Company_car
        fields = "__all__"