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
from .serializers import House_rent_extensionListSerializer, House_rent_extensionDetailSerializer

class House_rent_extension(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        all_house_rent_extensions = House_rent_extension.objects.all()
        serializer = House_rent_extensionListSerializer(all_house_rent_extensions, many=True, context={"request": request},)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = House_rent_extensionDetailSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
class House_rent_extensionDetail(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try: 
            return House_rent_extension.objects.get(pk=pk)
        except House_rent_extension.DoesNotExist:
            raise NotFound
    
    def get(self, request, pk):
        house_rent_extension = self.get_object(pk)
        serializer = House_rent_extensionDetailSerializer(house_rent_extension, context={"request": request},)
        return Response(serializer.data)

    def put(self, request, pk):
        house_rent_extension = self.get_object(pk)
        if house_rent_extension.responsible_person != request.user:
            raise PermissionDenied

    def delete(self, request, pk):
        house_rent_extension = self.get_object(pk)
        if house_rent_extension.responsible_person != request.user:
            raise PermissionDenied
        house_rent_extension.delete()
        return Response(status=HTTP_204_NO_CONTENT)