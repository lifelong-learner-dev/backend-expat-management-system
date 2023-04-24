from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Explanation, Document, Visit_place, Additional_information
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

class Additional_informationDetailSerializer(ModelSerializer):
    responsible_person = TinyUserSerializer(read_only=True)
    explanations = ExplanationSerializer(read_only=True, many=True,)
    documents = DocumentSerializer(read_only=True, many=True)
    visit_places = Visit_placeSerializer(read_only=True, many=True)

    is_responsible_person = SerializerMethodField()

    class Meta:
        model = Additional_information
        fields = "__all__"

    def get_is_responsible_person(self, additional_information):
        request = self.context.get("request")
        if request:
            return additional_information.responsible_person == request.user
        return False

class Additional_informationListSerializer(ModelSerializer):

    is_responsible_person = SerializerMethodField()

    class Meta:
        model = Additional_information
        fields = ("pk", "name", "subject", "responsible_person", "is_responsible_person", "explanations", "documents", "visit_places", "created_at", "updated_at",)

    def get_is_responsible_person(self, additional_information):
        request = self.context.get("request")
        return additional_information.responsible_person == request.user