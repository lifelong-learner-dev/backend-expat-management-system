import time
from django.conf import settings
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
from .models import Explanation, Work_permit
from .serializers import ExplanationSerializer, Work_permitDetailSerializer, Work_permitListSerializer

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

class Work_permits(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self, request):
        all_work_permits = Work_permit.objects.all()
        serializer = Work_permitListSerializer(all_work_permits, many=True, context={"request": request},)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = Work_permitDetailSerializer(data=request.data)
        if serializer.is_valid():
            try:
                with transaction.atomic():
                    work_permit = serializer.save(expat = request.user)
                    explanations = request.data.get("explanations")
                    for explanation_pk in explanations:
                        explanation = Explanation.objects.get(pk=explanation_pk)
                        work_permit.explanations.add(explanation)
                    serializer = Work_permitDetailSerializer(work_permit, context={"request": request},)
                    return Response(serializer.data)
            except ObjectDoesNotExist as e:
                if isinstance(e, Explanation.DoesNotExist):
                    raise ParseError("Explanation not found")
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class Work_permitDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try: 
            return Work_permit.objects.get(pk=pk)
        except Work_permit.DoesNotExist:
            raise NotFound
    
    def get(self, request, pk):
        work_permit = self.get_object(pk)
        serializer = Work_permitDetailSerializer(work_permit, context={"request": request},)
        return Response(serializer.data)

    def put(self, request, pk):
        work_permit = self.get_object(pk)
        if work_permit.expat != request.user  or not request.user.is_work_permits and not request.user.is_supporter:
            raise PermissionDenied

    def delete(self, request, pk):
        work_permit = self.get_object(pk)
        if work_permit.expat != request.user or not request.user.is_work_permits and not request.user.is_supporter :
            raise PermissionDenied
        work_permit.delete()
        return Response(status=HTTP_204_NO_CONTENT)
