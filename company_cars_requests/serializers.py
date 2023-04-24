from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Explanation, Document, Company_cars_request
from users.serializers import TinyUserSerializer

class ExplanationSerializer(ModelSerializer):
    class Meta:
        model = Explanation
        fields = "__all__"

class DocumentSerializer(ModelSerializer):
    class Meta:
        model = Document
        fields = "__all__"

class Company_cars_requestDetailSerializer(ModelSerializer):
    expat = TinyUserSerializer(read_only=True)
    explanations = ExplanationSerializer(read_only=True, many=True,)
    documents = DocumentSerializer(read_only=True, many=True)
    
    is_expat = SerializerMethodField()

    class Meta:
        model = Company_cars_request
        fields = "__all__"

    def get_is_expat(self, company_cars_request):
        request = self.context.get("request")
        if request:
            return company_cars_request.expat == request.user
        return False

class Company_cars_requestListSerializer(ModelSerializer):

    is_expat = SerializerMethodField()

    class Meta:
        model = Company_cars_request
        fields = ("pk", "name", "expat", "is_expat", "explanations", "documents", "created_at", "updated_at",)

    def get_is_expat(self, company_cars_request):
        request = self.context.get("request")
        return company_cars_request.expat == request.user