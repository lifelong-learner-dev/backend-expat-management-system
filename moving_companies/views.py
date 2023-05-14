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
from .models import Moving_company
from .serializers import Moving_companyDetailSerializer, Moving_companyListSerializer

class Moving_companys(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self, request):
        all_moving_companies = Moving_company.objects.all()
        serializer = Moving_companyListSerializer(all_moving_companies, many=True, context={"request": request},)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = Moving_companyDetailSerializer(data=request.data)
        if request.user.is_support and request.user.is_moving and serializer.is_valid():
                    moving_company = serializer.save()   
                    serializer = Moving_companyDetailSerializer(moving_company, context={"request": request},)
                    return Response(serializer.data)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
class Moving_companyDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try: 
            return Moving_company.objects.get(pk=pk)
        except Moving_company.DoesNotExist:
            raise NotFound
    
    def get(self, request, pk):
        moving_company = self.get_object(pk)
        serializer = Moving_companyDetailSerializer(moving_company, context={"request": request},)
        return Response(serializer.data)

    def put(self, request, pk):
        moving_company = self.get_object(pk)
        if not request.user.is_supporter and not request.user.is_moving:
            raise PermissionDenied
            

    def delete(self, request, pk):
        moving_company = self.get_object(pk)
        if not request.user.is_supporter and not request.user.is_moving:
            raise PermissionDenied
        moving_company.delete()
        return Response(status=HTTP_204_NO_CONTENT)