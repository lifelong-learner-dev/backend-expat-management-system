from rest_framework.serializers import ModelSerializer
from .models import Driving_licenses_preparation_document

class Driving_licenses_preparation_documentDetailSerializer(ModelSerializer):

    class Meta:
        model = Driving_licenses_preparation_document
        fields = "__all__"


class Driving_licenses_preparation_documentListSerializer(ModelSerializer):
    
    class Meta:
        model = Driving_licenses_preparation_document
        fields = ("pk", "name", "expat", "is_expat", "explanations", "documents", "created_at", "updated_at",)
