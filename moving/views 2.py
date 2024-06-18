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
from .models import Moving as MovingModel
from .models import Moving
from .serializers import MovingDetailSerializer, MovingListSerializer

class Moving(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self, request):
        all_movings = MovingModel.objects.all()
        serializer = MovingListSerializer(all_movings, many=True, context={"request": request},)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = MovingDetailSerializer(data=request.data)
        if serializer.is_valid():
                    moving = serializer.save(responsible_person = request.user)
                    serializer = MovingDetailSerializer(moving, context={"request": request},)
                    return Response(serializer.data)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    

class MovingDetail(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try: 
            return Moving.objects.get(pk=pk)
        except Moving.DoesNotExist:
            raise NotFound
    
    def get(self, request, pk):
        moving = self.get_object(pk)
        serializer = MovingDetailSerializer(moving, context={"request": request},)
        return Response(serializer.data)

    def put(self, request, pk):
        moving = self.get_object(pk)
        if moving.responsible_person != request.user:
            raise PermissionDenied

    def delete(self, request, pk):
        moving = self.get_object(pk)
        if moving.responsible_person != request.user:
            raise PermissionDenied
        moving.delete()
        return Response(status=HTTP_204_NO_CONTENT)