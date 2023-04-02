from rest_framework.views import APIView
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST
from rest_framework.response import Response
from rest_framework.exceptions import (
    NotFound,
    ParseError,
    PermissionDenied,
)
from .models import Clause, Explanation, Regulation, House
from .serializers import ClauseSerializer, ExplanationSerializer, RegulationSerializer

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
    pass
    
class HouseDetail(APIView):
    pass