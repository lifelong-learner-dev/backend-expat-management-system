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
from .models import Pick_ups_request
from .serializers import Pick_ups_requestDetailSerializer, Pick_ups_requestListSerializer

class Pick_ups_requests(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self, request):
        all_pick_ups_requests = Pick_ups_request.objects.all()
        serializer = Pick_ups_requestListSerializer(all_pick_ups_requests, many=True, context={"request": request},)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = Pick_ups_requestDetailSerializer(data=request.data)
        if serializer.is_valid():
                    pick_ups_request = serializer.save(expat = request.user)
                    serializer = Pick_ups_requestDetailSerializer(pick_ups_request, context={"request": request},)
                    return Response(serializer.data)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class Pick_ups_requestDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try: 
            return Pick_ups_request.objects.get(pk=pk)
        except Pick_ups_request.DoesNotExist:
            raise NotFound
    
    def get(self, request, pk):
        pick_ups_request = self.get_object(pk)
        serializer = Pick_ups_requestDetailSerializer(pick_ups_request, context={"request": request},)
        return Response(serializer.data)

    def put(self, request, pk):
        pick_ups_request = self.get_object(pk)
        if not request.user.is_supporter and not request.user.is_pick_ups or pick_ups_request.expat != request.user:
            raise PermissionDenied

    def delete(self, request, pk):
        pick_ups_request = self.get_object(pk)
        if not request.user.is_supporter and not request.user.is_pick_ups or pick_ups_request.expat != request.user:
            raise PermissionDenied
        pick_ups_request.delete()
        return Response(status=HTTP_204_NO_CONTENT)