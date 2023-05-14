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
from .models import Moving_request
from .serializers import Moving_requestDetailSerializer, Moving_requestListSerializer

class Moving_requests(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self, request):
        all_moving_requests = Moving_request.objects.all()
        serializer = Moving_requestListSerializer(all_moving_requests, many=True, context={"request": request},)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = Moving_requestDetailSerializer(data=request.data)
        if serializer.is_valid():
                    moving_request = serializer.save(expat = request.user)
                    serializer = Moving_requestDetailSerializer(moving_request, context={"request": request},)
                    return Response(serializer.data)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class Moving_requestDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try: 
            return Moving_request.objects.get(pk=pk)
        except Moving_request.DoesNotExist:
            raise NotFound
    
    def get(self, request, pk):
        moving_request = self.get_object(pk)
        serializer = Moving_requestDetailSerializer(moving_request, context={"request": request},)
        return Response(serializer.data)

    def put(self, request, pk):
        moving_request = self.get_object(pk)
        if not request.user.is_supporter and not request.user.is_moving or moving_request.expat != request.user:
            raise PermissionDenied

    def delete(self, request, pk):
        moving_request = self.get_object(pk)
        if not request.user.is_supporter and not request.user.is_moving or moving_request.expat != request.user:
            raise PermissionDenied
        moving_request.delete()
        return Response(status=HTTP_204_NO_CONTENT)
