from rest_framework.serializers import ModelSerializer
from .models import Explanation, Document, Visit_place, Announcement

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

class AnnouncementSerializer(ModelSerializer):
    class Meta:
        model = Announcement
        fields = "__all__"