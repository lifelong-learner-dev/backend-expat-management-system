from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Explanation, Document, Family_residence_permits_request
from users.serializers import TinyUserSerializer

class ExplanationSerializer(ModelSerializer):
    class Meta:
        model = Explanation
        fields = "__all__"

class DocumentSerializer(ModelSerializer):
    class Meta:
        model = Document
        fields = "__all__"

class Family_residence_permits_requestDetailSerializer(ModelSerializer):
    expat = TinyUserSerializer(read_only=True)
    explanations = ExplanationSerializer(read_only=True, many=True,)
    documents = DocumentSerializer(read_only=True, many=True)

    is_expat = SerializerMethodField()

    class Meta:
        model = Family_residence_permits_request
        fields = "__all__"

    def get_is_expat(self, family_residence_permits_request):
        request = self.context.get("request")
        if request:
            return Family_residence_permits_request.expat == request.user
        return False

class Family_residence_permits_requestListSerializer(ModelSerializer):

    is_expat = SerializerMethodField()

    class Meta:
        model = Family_residence_permits_request
        fields = ("pk", "name", "expat", "is_expat", "expalanations", "documents", "create_at", "updated_at",)

    def get_is_expat(self, family_residence_permits_request):
        request = self.context.get("request")
        return family_residence_permits_request.expat == request.user