from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Announcement
from users.serializers import TinyUserSerializer

class AnnouncementDetailSerializer(ModelSerializer):
    responsible_person = TinyUserSerializer(read_only=True)
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
        fields =  "__all__"
        
    def get_is_responsible_person(self, announcement):
        request = self.context.get("request")
        return announcement.responsible_person == request.user