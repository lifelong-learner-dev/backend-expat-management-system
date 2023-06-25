from rest_framework.serializers import ModelSerializer
from .models import Family_residence_permits_preparation_document

class Family_residence_permits_preparation_documentDetailSerializer(ModelSerializer):

    class Meta:
        model = Family_residence_permits_preparation_document
        fields = "__all__"


class Family_residence_permits_preparation_documentListSerializer(ModelSerializer):
    
    class Meta:
        model = Family_residence_permits_preparation_document
        fields = ("pk", "name", "expat", "is_expat", "created_at", "updated_at",)
