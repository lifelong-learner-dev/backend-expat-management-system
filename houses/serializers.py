from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Clause, Explanation, Regulation, House
from users.serializers import TinyUserSerializer

class ClauseSerializer(ModelSerializer):
    class Meta:
        model = Clause
        fields = "__all__"

class ExplanationSerializer(ModelSerializer):
    class Meta:
        model = Explanation
        fields = "__all__"

class RegulationSerializer(ModelSerializer):
    class Meta:
        model = Regulation
        fields = "__all__"

class HouseDetailSerializer(ModelSerializer):
    responsible_person = TinyUserSerializer(read_only=True)
    explanations = ExplanationSerializer(read_only=True, many=True,)
    clauses = ClauseSerializer(read_only=True, many=True)
    regulations = RegulationSerializer(read_only=True, many=True)

    is_responsible_person = SerializerMethodField()

    class Meta:
        model = House
        fields = "__all__"

    def get_is_responsible_person(self, house):
        request = self.context.get("request")
        if request:
            return house.responsible_person == request.user
        return False


class HouseListSerializer(ModelSerializer):

    is_responsible_person = SerializerMethodField()

    class Meta:
        model = House
        fields = ("pk", "name", "subject", "responsible_person", "is_responsible_person", "explanations", "clauses", "regulations", "created_at", "updated_at",)

    def get_is_responsible_person(self, house):
        request = self.context.get("request")
        return house.responsible_person == request.user