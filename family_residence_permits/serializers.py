from rest_framework.serializers import ModelSerializer
from .models import Explanation, Document, Visit_place, Family_residence_permit

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

class Family_residence_permitSerializer(ModelSerializer):
    class Meta:
        model = Family_residence_permit
        fields = "__all__"