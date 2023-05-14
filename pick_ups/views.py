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
from .models import Explanation, Pick_up
from .serializers import ExplanationSerializer, Pick_upListSerializer, Pick_upDetailSerializer

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

class Pick_ups(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self, request):
        all_pick_ups = Pick_up.objects.all()
        serializer = Pick_upListSerializer(all_pick_ups, many=True, context={"request": request},)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = Pick_upDetailSerializer(data=request.data)
        if serializer.is_valid():
            try:
                with transaction.atomic():
                    pick_up = serializer.save(expat = request.user)
                    explanations = request.data.get("explanations")
                    for explanation_pk in explanations:
                        explanation = Explanation.objects.get(pk=explanation_pk)
                        pick_up.explanations.add(explanation)    
                    serializer = Pick_upDetailSerializer(pick_up, context={"request": request},)
                    return Response(serializer.data)
            except ObjectDoesNotExist as e:
                if isinstance(e, Explanation.DoesNotExist):
                    raise ParseError("Explanation not found")
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class Pick_upDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try: 
            return Pick_up.objects.get(pk=pk)
        except Pick_up.DoesNotExist:
            raise NotFound
    
    def get(self, request, pk):
        pick_up = self.get_object(pk)
        serializer = Pick_upDetailSerializer(pick_up, context={"request": request},)
        return Response(serializer.data)

    def put(self, request, pk):
        pick_up = self.get_object(pk)
        if pick_up.expat != request.user:
            raise PermissionDenied

    def delete(self, request, pk):
        pick_up = self.get_object(pk)
        if pick_up.expat != request.user:
            raise PermissionDenied
        pick_up.delete()
        return Response(status=HTTP_204_NO_CONTENT)