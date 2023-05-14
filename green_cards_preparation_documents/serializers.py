from rest_framework.serializers import ModelSerializer
from .models import Green_cards_preparation_document

class Green_cards_preparation_documentDetailSerializer(ModelSerializer):

    class Meta:
        model = Green_cards_preparation_document
        fields = "__all__"


class Green_cards_preparation_documentListSerializer(ModelSerializer):
    
    class Meta:
        model = Green_cards_preparation_document
        fields = ("pk", "name", "expat", "is_expat", "explanations", "documents", "created_at", "updated_at",)
