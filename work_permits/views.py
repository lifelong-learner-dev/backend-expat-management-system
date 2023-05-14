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
from .models import Work_permit
from .serializers import Work_permitDetailSerializer, Work_permitListSerializer

class Work_permits(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self, request):
        all_work_permits = Work_permit.objects.all()
        serializer = Work_permitListSerializer(all_work_permits, many=True, context={"request": request},)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = Work_permitDetailSerializer(data=request.data)
        if serializer.is_valid():
                    work_permit = serializer.save(expat = request.user)
                    serializer = Work_permitDetailSerializer(work_permit, context={"request": request},)
                    return Response(serializer.data)
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
