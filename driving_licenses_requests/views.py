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
from .models import Driving_licenses_request
from .serializers import Driving_licenses_requestDetailSerializer, Driving_licenses_requestListSerializer

class Driving_licenses_requests(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self, request):
        all_driving_licenses_requests = Driving_licenses_request.objects.all()
        serializer = Driving_licenses_requestListSerializer(all_driving_licenses_requests, many=True, context={"request": request},)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = Driving_licenses_requestDetailSerializer(data=request.data)
        if serializer.is_valid():
                    driving_licenses_request = serializer.save(expat = request.user)   
                    serializer = Driving_licenses_requestDetailSerializer(driving_licenses_request, context={"request": request},)
                    return Response(serializer.data)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class Driving_licenses_requestDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try: 
            return Driving_licenses_request.objects.get(pk=pk)
        except Driving_licenses_request.DoesNotExist:
            raise NotFound
    
    def get(self, request, pk):
        driving_licenses_request = self.get_object(pk)
        serializer = Driving_licenses_requestDetailSerializer(driving_licenses_request, context={"request": request},)
        return Response(serializer.data)

    def put(self, request, pk):
        driving_licenses_request = self.get_object(pk)
        if driving_licenses_request.expat != request.user:
            raise PermissionDenied

    def delete(self, request, pk):
        driving_licenses_request = self.get_object(pk)
        if driving_licenses_request.expat != request.user:
            raise PermissionDenied
        driving_licenses_request.delete()
        return Response(status=HTTP_204_NO_CONTENT)