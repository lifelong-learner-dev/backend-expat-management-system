from rest_framework.serializers import ModelSerializer
from .models import Explanation, Document, Family_residence_permits_request

class ExplanationSerializer(ModelSerializer):
    class Meta:
        model = Explanation
        fields = "__all__"

class DocumentSerializer(ModelSerializer):
    class Meta:
        model = Document
        fields = "__all__"

class Family_residence_permits_requestSerializer(ModelSerializer):
    class Meta:
        model = Family_residence_permits_request
        fields = "__all__"