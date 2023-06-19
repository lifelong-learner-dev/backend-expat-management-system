from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Company_cars_supporter
from users.serializers import TinyUserSerializer

class Company_cars_supporterDetailSerializer(ModelSerializer):
    responsible_person = TinyUserSerializer(read_only=True) 
    is_responsible_person = SerializerMethodField()

    class Meta:
        model = Company_cars_supporter
        fields = "__all__"

    def get_is_responsible_person(self, company_cars_supporter):
        request = self.context.get("request")
        if request:
            return company_cars_supporter.responsible_person == request.user
        return False

class Company_cars_supporterListSerializer(ModelSerializer):

    is_responsible_person = SerializerMethodField()

    class Meta:
        model = Company_cars_supporter
        fields = ("pk", "name", "responsible_person", "is_responsible_person", "created_at", "updated_at",)

    def get_is_responsible_person(self, company_cars_supporter):
        request = self.context.get("request")
        return company_cars_supporter.responsible_person == request.user