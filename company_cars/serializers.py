from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Explanation, Document, Company_car
from users.serializers import TinyUserSerializer

class ExplanationSerializer(ModelSerializer):
    class Meta:
        model = Explanation
        fields = "__all__"

class DocumentSerializer(ModelSerializer):
    class Meta:
        model = Document
        fields = "__all__"

class Company_carDetailSerializer(ModelSerializer):
    responsible_person = TinyUserSerializer(read_only=True)
    explanations = ExplanationSerializer(read_only=True, many=True,)
    documents = DocumentSerializer(read_only=True, many=True)
    
    is_responsible_person = SerializerMethodField()

    class Meta:
        model = Company_car
        fields = "__all__"

    def get_is_responsible_person(self, company_car):
        request = self.context.get("request")
        if request:
            return company_car.responsible_person == request.user
        return False

class Company_carListSerializer(ModelSerializer):

    is_responsible_person = SerializerMethodField()

    class Meta:
        model = Company_car
        fields = ("pk", "name", "responsible_person", "is_responsible_person", "explanations", "documents", "created_at", "updated_at",)

    def get_is_responsible_person(self, company_car):
        request = self.context.get("request")
        return company_car.responsible_person == request.user