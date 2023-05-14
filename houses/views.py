import time
from django.conf import settings
from django.utils import timezone
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from django.db import transaction
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST
from rest_framework.response import Response
from rest_framework.exceptions import (
    NotFound,
    ParseError,
    PermissionDenied,
)
from .models import Clause, Explanation, Regulation, House
from .serializers import ClauseSerializer, ExplanationSerializer, RegulationSerializer, HouseDetailSerializer, HouseListSerializer

class Clauses(APIView):
    def get(self, request):
        all_clauses = Clause.objects.all()
        serializer = ClauseSerializer(all_clauses, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ClauseSerializer(data=request.data)
        if serializer.is_valid():
           clause = serializer.save()
           return Response(ClauseSerializer(clause).data)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class ClauseDetail(APIView):
    def get_object(self, pk):
        try: 
            return Clause.objects.get(pk=pk)
        except Clause.DoesNotExist:
            raise NotFound
    
    def get(self, request, pk):
        clause = self.get_object(pk)
        serializer = ClauseSerializer(clause)
        return Response(serializer.data)

    def put(self, request, pk):
        clause = self.get_object(pk)
        serializer = ClauseSerializer(clause, data=request.data, partial=True)
        if serializer.is_valid():
            updated_clause = serializer.save()
            return Response(ClauseSerializer(updated_clause).data,)
        else:
          return Response(serializer.error)  

    def delete(self, request, pk):
        clause = self.get_object(pk)
        clause.delete()
        return Response(status=HTTP_204_NO_CONTENT)


class Explanations(APIView):
    def get(self, request):
        all_explanations = Explanation.objects.all()
        serializer = ExplanationSerializer(all_explanations, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ExplanationSerializer(data=request.data)
        if serializer.is_valid():
           explanation = serializer.save()
           return Response(ExplanationSerializer(explanation).data)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class ExplanationDetail(APIView):
    def get_object(self, pk):
        try: 
            return Explanation.objects.get(pk=pk)
        except Explanation.DoesNotExist:
            raise NotFound
    
    def get(self, request, pk):
        explanation = self.get_object(pk)
        serializer = ExplanationSerializer(explanation)
        return Response(serializer.data)

    def put(self, request, pk):
        explanation = self.get_object(pk)
        serializer = ExplanationSerializer(explanation, data=request.data, partial=True)
        if serializer.is_valid():
            updated_explanation = serializer.save()
            return Response(ExplanationSerializer(updated_explanation).data,)
        else:
          return Response(serializer.error)  

    def delete(self, request, pk):
        explanation = self.get_object(pk)
        explanation.delete()
        return Response(status=HTTP_204_NO_CONTENT)

class Regulations(APIView):
    def get(self, request):
        all_regulations = Regulation.objects.all()
        serializer = RegulationSerializer(all_regulations, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = RegulationSerializer(data=request.data)
        if serializer.is_valid():
           regulation = serializer.save()
           return Response(RegulationSerializer(regulation).data)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class RegulationDetail(APIView):
    def get_object(self, pk):
        try: 
            return Regulation.objects.get(pk=pk)
        except Regulation.DoesNotExist:
            raise NotFound
    
    def get(self, request, pk):
        regulation = self.get_object(pk)
        serializer = RegulationSerializer(regulation)
        return Response(serializer.data)

    def put(self, request, pk):
        regulation = self.get_object(pk)
        serializer = RegulationSerializer(regulation, data=request.data, partial=True)
        if serializer.is_valid():
            updated_regulation = serializer.save()
            return Response(RegulationSerializer(updated_regulation).data,)
        else:
          return Response(serializer.error)  

    def delete(self, request, pk):
        regulation = self.get_object(pk)
        regulation.delete()
        return Response(status=HTTP_204_NO_CONTENT)

class Houses(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self, request):
        all_houses = House.objects.all()
        serializer = HouseListSerializer(all_houses, many=True, context={"request": request},)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = HouseDetailSerializer(data=request.data)
        if serializer.is_valid():
            try:
                with transaction.atomic():
                    house = serializer.save(responsible_person = request.user)
                    explanations = request.data.get("explanations")
                    for explanation_pk in explanations:
                        explanation = Explanation.objects.get(pk=explanation_pk)
                        house.explanations.add(explanation)
                    clauses = request.data.get("clauses")
                    for clause_pk in clauses:
                        clause = Clause.objects.get(pk=clause_pk)
                        house.clauses.add(clause)
                    regulations = request.data.get("regulations")
                    for regulation_pk in regulations:
                        regulation = Regulation.objects.get(pk=regulation_pk)
                        house.regulations.add(regulation)    
                    serializer = HouseDetailSerializer(house, context={"request": request},)
                    return Response(serializer.data)
            except ObjectDoesNotExist as e:
                if isinstance(e, Explanation.DoesNotExist):
                    raise ParseError("Explanation not found")
                elif isinstance(e, Clause.DoesNotExist):
                    raise ParseError("Clause not found") 
                elif isinstance(e, Regulation.DoesNotExist):
                    raise ParseError("Regulation not found") 
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
    
class HouseDetail(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try: 
            return House.objects.get(pk=pk)
        except House.DoesNotExist:
            raise NotFound
    
    def get(self, request, pk):
        house = self.get_object(pk)
        serializer = HouseDetailSerializer(house, context={"request": request},)
        return Response(serializer.data)

    def put(self, request, pk):
        house = self.get_object(pk)
        if house.responsible_person != request.user:
            raise PermissionDenied

    def delete(self, request, pk):
        house = self.get_object(pk)
        if house.responsible_person != request.user:
            raise PermissionDenied
        house.delete()
        return Response(status=HTTP_204_NO_CONTENT)