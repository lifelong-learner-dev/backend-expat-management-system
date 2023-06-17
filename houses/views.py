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
from .models import House
from .serializers import HouseDetailSerializer, HouseListSerializer

class Houses(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self, request):
        all_houses = House.objects.all()
        serializer = HouseListSerializer(all_houses, many=True, context={"request": request},)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = HouseDetailSerializer(data=request.data)
        if serializer.is_valid():
                with transaction.atomic():
                    house = serializer.save(responsible_person = request.user)   
                    serializer = HouseDetailSerializer(house, context={"request": request},)
                    return Response(serializer.data)
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