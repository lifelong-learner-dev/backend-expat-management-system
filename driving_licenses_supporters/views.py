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
from .models import Driving_licenses_supporter
from .serializers import Driving_licenses_supporterDetailSerializer, Driving_licenses_supporterListSerializer

class Driving_licenses_supporters(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self, request):
        all_driving_licenses_supporters = Driving_licenses_supporter.objects.all()
        serializer = Driving_licenses_supporterListSerializer(all_driving_licenses_supporters, many=True, context={"request": request},)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = Driving_licenses_supporterDetailSerializer(data=request.data)
        if serializer.is_valid():
                    driving_licenses_supporter = serializer.save(responsible_person = request.user)   
                    serializer = Driving_licenses_supporterDetailSerializer(driving_licenses_supporter, context={"request": request},)
                    return Response(serializer.data)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
class Driving_licenses_supporterDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try: 
            return Driving_licenses_supporter.objects.get(pk=pk)
        except Driving_licenses_supporter.DoesNotExist:
            raise NotFound
    
    def get(self, request, pk):
        driving_licenses_supporter = self.get_object(pk)
        serializer = Driving_licenses_supporterDetailSerializer(driving_licenses_supporter, context={"request": request},)
        return Response(serializer.data)

    def put(self, request, pk):
        driving_licenses_supporter = self.get_object(pk)
        if driving_licenses_supporter.responsible_person != request.user:
            raise PermissionDenied

    def delete(self, request, pk):
        driving_licenses_supporter = self.get_object(pk)
        if driving_licenses_supporter.responsible_person != request.user:
            raise PermissionDenied
        driving_licenses_supporter.delete()
        return Response(status=HTTP_204_NO_CONTENT)