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
from .models import Driving_license
from .serializers import Driving_licenseDetailSerializer, Driving_licenseListSerializer

class Driving_licenses(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self, request):
        all_driving_licenses = Driving_license.objects.all()
        serializer = Driving_licenseListSerializer(all_driving_licenses, many=True, context={"request": request},)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = Driving_licenseDetailSerializer(data=request.data)
        if serializer.is_valid():
                    driving_license = serializer.save(expat = request.user) 
                    serializer = Driving_licenseDetailSerializer(driving_license, context={"request": request},)
                    return Response(serializer.data)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class Driving_licenseDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try: 
            return Driving_license.objects.get(pk=pk)
        except Driving_license.DoesNotExist:
            raise NotFound
    
    def get(self, request, pk):
        driving_license = self.get_object(pk)
        serializer = Driving_licenseDetailSerializer(driving_license, context={"request": request},)
        return Response(serializer.data)

    def put(self, request, pk):
        driving_license = self.get_object(pk)
        if driving_license.expat != request.user:
            raise PermissionDenied

    def delete(self, request, pk):
        driving_license = self.get_object(pk)
        if driving_license.expat != request.user:
            raise PermissionDenied
        driving_license.delete()
        return Response(status=HTTP_204_NO_CONTENT)