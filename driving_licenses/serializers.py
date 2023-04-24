from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Explanation, Document, Visit_place, Driving_license
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

class Driving_licenseDetailSerializer(ModelSerializer):
    expat = TinyUserSerializer(read_only=True)
    explanations = ExplanationSerializer(read_only=True, many=True,)
    documents = DocumentSerializer(read_only=True, many=True)
    
    is_expat = SerializerMethodField()

    class Meta:
        model = Driving_license
        fields = "__all__"

    def get_is_expat(self, driving_license):
        request = self.context.get("request")
        if request:
            return driving_license.expat == request.user
        return False

class Driving_licenseListSerializer(ModelSerializer):

    is_expat = SerializerMethodField()

    class Meta:
        model = Driving_license
        fields = ("pk", "name", "expat", "is_expat", "explanations", "documents", "created_at", "updated_at",)

    def get_is_expat(self, driving_license):
        request = self.context.get("request")
        return driving_license.expat == request.user