from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Explanation, Document, Visit_place, Family_residence_permit
from users.serializers import TinyUserSerializer

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

class Family_residence_permitDetailSerializer(ModelSerializer):
    expat = TinyUserSerializer(read_only=True)
    explanations = ExplanationSerializer(read_only=True, many=True,)
    documents = DocumentSerializer(read_only=True, many=True)
    visit_places = Visit_placeSerializer(read_only=True, many=True)

    is_expat = SerializerMethodField()

    class Meta:
        model = Family_residence_permit
        fields = "__all__"

    def get_is_expat(self, family_residence_permit):
        request = self.context.get("request")
        if request:
            return family_residence_permit.expat == request.user
        return False


class Family_residence_permitListSerializer(ModelSerializer):

    is_expat = SerializerMethodField()

    class Meta:
        model = Family_residence_permit
        fields = ("pk", "name", "expat", "is_expat", "explanations", "documents", "created_at", "updated_at",)

    def get_is_expat(self, family_residence_permit):
        request = self.context.get("request")
        return family_residence_permit.expat == request.user