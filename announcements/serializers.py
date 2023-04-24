from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Explanation, Document, Visit_place, Announcement
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

class AnnouncementDetailSerializer(ModelSerializer):
    responsible_person = TinyUserSerializer(read_only=True)
    explanations = ExplanationSerializer(read_only=True, many=True,)
    documents = DocumentSerializer(read_only=True, many=True)
    visit_places = Visit_placeSerializer(read_only=True, many=True)

    is_responsible_person = SerializerMethodField()

    class Meta:
        model = Announcement
        fields = "__all__"

    def get_is_responsible_person(self, announcement):
        request = self.context.get("request")
        if request:
            return announcement.responsible_person == request.user
        return False

class AnnouncementListSerializer(ModelSerializer):

    is_responsible_person = SerializerMethodField()

    class Meta:
        model = Announcement
        fields = ("pk", "name", "subject", "responsible_person", "is_responsible_person", "explanations", "documents", "visit_places", "created_at", "updated_at",)

    def get_is_responsible_person(self, announcement):
        request = self.context.get("request")
        return announcement.responsible_person == request.user