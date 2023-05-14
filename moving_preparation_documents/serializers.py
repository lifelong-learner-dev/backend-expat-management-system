from rest_framework.serializers import ModelSerializer
from .models import Moving_preparation_document

class Moving_preparation_documentDetailSerializer(ModelSerializer):

    class Meta:
        model = Moving_preparation_document
        fields = "__all__"


class Moving_preparation_documentListSerializer(ModelSerializer):
    
    class Meta:
        model = Moving_preparation_document
        fields = ("pk", "name", "expat", "is_expat", "explanations", "documents", "created_at", "updated_at",)
