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
from .models import Work_permits_request
from .serializers import Work_permits_requestDetailSerializer, Work_permits_requestListSerializer

class Work_permits_requests(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self, request):
        all_work_permits_requests = Work_permits_request.objects.all()
        serializer = Work_permits_requestListSerializer(all_work_permits_requests, many=True, context={"request": request},)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = Work_permits_requestDetailSerializer(data=request.data)
        if serializer.is_valid():
                    work_permits_request = serializer.save(expat = request.user)
                    serializer = Work_permits_requestDetailSerializer(work_permits_request, context={"request": request},)
                    return Response(serializer.data)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class Work_permits_requestDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try: 
            return Work_permits_request.objects.get(pk=pk)
        except Work_permits_request.DoesNotExist:
            raise NotFound
    
    def get(self, request, pk):
        work_permits_request = self.get_object(pk)
        serializer = Work_permits_requestDetailSerializer(work_permits_request, context={"request": request},)
        return Response(serializer.data)

    def put(self, request, pk):
        work_permits_request = self.get_object(pk)
        if not request.user.is_supporter and not request.user.is_work_permits or work_permits_request.expat != request.user:
            raise PermissionDenied

    def delete(self, request, pk):
        work_permits_request = self.get_object(pk)
        if not request.user.is_supporter and not request.user.is_work_permits or work_permits_request.expat != request.user:
            raise PermissionDenied
        work_permits_request.delete()
        return Response(status=HTTP_204_NO_CONTENT)